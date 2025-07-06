import sys
sys.path.insert(0, '/home/nnutannep/Github/simple-semi-simple')

# Import SageMath and custom functions
from custom_matroid_functions import *
from sage.combinat.posets.moebius_algebra import *
from sage.matroids.constructor import Matroid

class ChowBasis(BasisAbstract):
    """
    The Chow basis for the Deformed Möbius Algebra (Chow ring context).
    """
    def __init__(self, M, prefix='C') -> None:
        self._basis_name = "chow"
        # The basis could be indexed by flags, or by certain monomials in x_F
        # For now, let's assume it's indexed by flats (like the zeta basis)
        CombinatorialFreeModule.__init__(self, M.base_ring(),
                                        tuple(M._lattice),
                                        prefix=prefix,
                                        category=MoebiusAlgebraBases(M))

        # Change of basis:
        E = M.E()
        phi = self.module_morphism(self._to_natural_basis,
                                codomain=E, category=self.category(),
                                triangular='upper', unitriangular=True,
                                key=M._lattice._element_to_vertex)

        phi.register_as_coercion()
        (~phi).register_as_coercion()

    def _to_natural_basis(self, F):
        M = self.realization_of()
        L = M._lattice
        E = M.E()
        q = M._q
        rank = L.rank_function()
        matroid = M._matroid
        R = M.base_ring()
        # For each G ≤ F, get the Poincaré polynomial of the contraction M^F_G
        return E.sum_of_terms(
            (G, q**(1 * (rank(F) - rank(G))) *
            R(poincare_polynomial_of_minor(matroid, F, G)(q**-2)))
            for G in L.order_ideal([F])
        )

class ZetaBasis(BasisAbstract):
    """
    The zeta basis for the Quantum Möbius Algebra.
    """
    def __init__(self, M, prefix='Z') -> None:
        self._basis_name = "zeta"
        CombinatorialFreeModule.__init__(self, M.base_ring(),
                                        tuple(M._lattice),
                                        prefix=prefix,
                                        category=MoebiusAlgebraBases(M))

        # Change of basis:
        E = M.E()
        phi = self.module_morphism(self._to_natural_basis,
                                codomain=E, category=self.category(),
                                triangular='upper', unitriangular=True,
                                key=M._lattice._element_to_vertex)

        phi.register_as_coercion()
        (~phi).register_as_coercion()

    def _to_natural_basis(self, x):
        M = self.realization_of()
        L = M._lattice
        E = M.E()
        q = M._q
        rank = L.rank_function()
        return E.sum_of_terms(
            (y, q**(rank(x) - rank(y)) *
            L.kazhdan_lusztig_polynomial(y, x)(q=q**-2))
            for y in L.order_ideal([x])
        )

class DeformedMoebiusAlgebra(QuantumMoebiusAlgebra):
    """
    A class representing the Deformed Möbius Algebra with the Zeta basis.
    Can be constructed from either a matroid or a lattice of flats.
    """
    def __init__(self, matroid, base_ring=None):
        """
        Initialize the Deformed Möbius Algebra from a matroid.
        The lattice of flats is automatically extracted from the matroid.
        """
        if base_ring is None:
            self._R = LaurentPolynomialRing(ZZ, 'x')
        else:
            self._R = base_ring
        x = self._R.gen()

        # Store the matroid and get its lattice of flats
        self._matroid = matroid
        self._lattice = matroid.lattice_of_flats()

        super().__init__(self._lattice, x)
        self._chow_basis = ChowBasis(self)
        self._zeta_basis = ZetaBasis(self)

    def C(self):
        """
        Returns the Chow basis for this algebra.
        """
        return self._chow_basis

    def zeta(self):
        """
        Return the zeta basis for this algebra.
        """
        return self._zeta_basis

    def is_in_Hp(self, alpha):
        """
        Check if an element alpha belongs to the Hodge-Poincaré space H_p.
        
        INPUT:
        - alpha: an element of the algebra
        
        OUTPUT:
        - True if alpha is in H_p, False otherwise
        
        The Hodge-Poincaré space H_p consists of elements that satisfy
        certain palindromic conditions with respect to the lattice structure.
        For perverse elements, we check that the coefficients are palindromic
        with respect to the rank differences.
        """
        E = self.E()
        L = self._lattice
        t = self._q
        rank_func = L.rank_function()
        
        alpha_dict = E(alpha).monomial_coefficients()
        
        for F in alpha_dict.keys():
            for G in L.order_filter([F]):
                if G in alpha_dict and not isinstance(alpha_dict[G], type(t**0)):
                    try:
                        alpha_dict[G].subs({t: 0})
                    except (TypeError, ValueError):
                        print(f"Coefficient for G={G} is not a polynomial: {alpha_dict[G]}")
                        return False

            sum_S_F = 0
            rank_F = rank_func(F)

            for G in L.order_filter([F]):
                coeff_G = alpha_dict.get(G, 0) # Get coefficient alpha_G, default to 0
                if coeff_G != 0:
                    rank_G = rank_func(G)
                    term = coeff_G * (t**(1 * (rank_F - rank_G)))
                    sum_S_F += term
            try:
                # Check if the sum is palindromic (invariant under t -> 1/t)
                if sum_S_F != sum_S_F.subs({t: 1/t}):
                    print(f"Palindromic check failed for F={F}")
                    print(f"Sum = {sum_S_F}")
                    print(f"Sum(1/t) = {sum_S_F.subs({t: 1/t})}")
                    return False
            except Exception as e:
                print(f"Error during palindromic check for F={F}: {e}")
                return False

        return True

# Utility functions for working with the algebra
def create_deformed_algebra(matroid, base_ring=None):
    """
    Create a DeformedMoebiusAlgebra from a matroid.
    
    INPUT:
    - matroid: a SageMath matroid
    - base_ring: optional base ring (default: LaurentPolynomialRing(ZZ, 'x'))
    
    OUTPUT:
    - DeformedMoebiusAlgebra instance
    """
    return DeformedMoebiusAlgebra(matroid, base_ring=base_ring)

def create_deformed_algebra_from_lattice(lattice, base_ring=None):
    """
    Create a DeformedMoebiusAlgebra from a lattice of flats.
    
    INPUT:
    - lattice: a lattice of flats
    - base_ring: optional base ring (default: LaurentPolynomialRing(ZZ, 'x'))
    
    OUTPUT:
    - DeformedMoebiusAlgebra instance
    """
    matroid = Matroid(lattice)
    return DeformedMoebiusAlgebra(matroid, base_ring=base_ring)

# Define what should be imported when using "from HM_module import *"
__all__ = [
    'ChowBasis',
    'ZetaBasis', 
    'DeformedMoebiusAlgebra',
    'create_deformed_algebra',
    'create_deformed_algebra_from_lattice'
]