#!/usr/bin/env sage

import sys
sys.path.insert(0, '/home/nnutannep/Github/simple-semi-simple')

from HM_module import *
from custom_matroid_functions import *

# Set up the same example as in the notebook
P = LaurentPolynomialRing(ZZ, 'x')
x = P.gen() 
k, n = 4, 3
M = matroids.CompleteGraphic(n)
r = M.rank()

e = next(x for x in M.groundset() if x not in M.coloops())
print(f"Original matroid groundset: {M.groundset()}")
print(f"Deleting element: {e}")

mdele = M.delete(e)
L = M.lattice_of_flats()
Ldel_e = mdele.lattice_of_flats()

Eq_M = create_deformed_algebra(M, base_ring=P)
Eq_mdele = create_deformed_algebra(mdele, base_ring=P)

# Test the problematic conversion
print("\n=== Testing the problematic conversion ===")
E = Eq_M.natural()
C = Eq_M.C()
C_dele = Eq_mdele.C()
E_mdele = Eq_mdele.natural()
E_mdele_basis = E_mdele.basis()

# Define a simpler delta function that works directly with natural basis
def delta_flat_simple(F):
    """Simple delta function that works directly with natural basis"""
    F_del_e = frozenset(set(F) - {e})
    if F_del_e not in Ldel_e:
        return E_mdele.zero()
    return x**(- M.rank(F) + mdele.rank(F_del_e)) * E_mdele_basis[F_del_e]

def delta_simple(elem):
    """Simple delta that works with natural basis elements"""
    # elem should already be in natural basis
    decom = elem.monomial_coefficients()
    return E_mdele.sum(coeff * delta_flat_simple(F) for F, coeff in decom.items())

# Define the original delta function (same as in notebook)
rev = {value: key for key, value in E.basis().items()}

def delta_flat(F):
    F_del_e = frozenset(set(F) - {e})
    assert F_del_e in Ldel_e
    return Eq_mdele(x**(- M.rank(F) + mdele.rank(F_del_e)) * E_mdele_basis[F_del_e])
    
def delta(elem):
    rep = E(elem)
    decom = {monomial: coeff for monomial, coeff in zip(rep.monomials(), rep.coefficients())}
    return Eq_mdele.sum(decom[F] * delta_flat(rev[F]) for F in decom)

# Test with a simple element first
test_flat = list(E.basis().keys())[2]  # Take the third flat
print(f"Testing with flat: {test_flat}")

try:
    # Test the simple approach
    print("Testing simple delta approach...")
    # Start with natural basis element
    natural_elem = E.basis()[test_flat]
    print(f"Natural basis element: {natural_elem}")
    
    # Apply delta
    delta_result = delta_simple(natural_elem)
    print(f"Delta result: {delta_result}")
    
    # Convert to Chow basis using safe method
    chow_result = Eq_mdele.safe_basis_conversion(delta_result, 'C')
    print(f"Chow basis result: {chow_result}")
    
    print("SUCCESS!")
except Exception as e:
    print(f"ERROR: {e}")
    print("This confirms the infinite loop issue.")

print("\n=== Testing the original problematic approach ===")
try:
    # This is what was causing the infinite loop
    print("Attempting original delta approach...")
    original_delta_result = delta(C[test_flat])
    print("SUCCESS with original approach!")
    print(f"Result: {original_delta_result}")
except Exception as e:
    print(f"ERROR with original approach: {e}")

print("\n=== Summary ===")
print("The issue is that the original delta function tries to convert")
print("Chow basis elements to natural basis, which involves complex")
print("polynomial computations that cause infinite loops.")
print("The solution is to work directly with natural basis elements.") 