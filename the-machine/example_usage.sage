#!/usr/bin/env sage
"""
Example usage of HM_module.py

This file demonstrates how to import and use the HM_module from other files.
"""

import sys
sys.path.insert(0, '/home/nnutannep/Github/simple-semi-simple/the-machine')

# Import the module
from HM_module import *

def main():
    """
    Example usage of the DeformedMoebiusAlgebra and its bases.
    """
    print("=== HM Module Example Usage ===\n")
    
    # Create a simple matroid
    M = matroids.Uniform(2, 4)
    print(f"Created matroid: {M}")
    print(f"Ground set: {M.groundset()}")
    print(f"Rank: {M.rank()}\n")
    
    # Create the deformed algebra
    algebra = create_deformed_algebra(M)
    print(f"Created algebra: {algebra}")
    print(f"Base ring: {algebra.base_ring()}\n")
    
    # Access the bases
    C = algebra.C()  # Chow basis
    Z = algebra.zeta()  # Zeta basis
    E = algebra.natural()  # Natural basis
    
    print("Bases available:")
    print(f"- Chow basis: {C}")
    print(f"- Zeta basis: {Z}")
    print(f"- Natural basis: {E}\n")
    
    # Get basis elements
    C_basis = C.basis()
    Z_basis = Z.basis()
    E_basis = E.basis()
    
    print("Basis elements:")
    print(f"Chow basis elements: {list(C_basis.keys())}")
    print(f"Zeta basis elements: {list(Z_basis.keys())}")
    print(f"Natural basis elements: {list(E_basis.keys())}\n")
    
    # Example: Convert between bases
    print("=== Basis Conversions ===")
    
    # Get a specific element in Chow basis
    F = frozenset([0, 1])
    if F in C_basis:
        chow_element = C[F]
        print(f"Chow basis element C[{F}]: {chow_element}")
        
        # Convert to natural basis
        natural_element = E(chow_element)
        print(f"In natural basis: {natural_element}")
        
        # Convert to zeta basis
        zeta_element = Z(chow_element)
        print(f"In zeta basis: {zeta_element}\n")
    
    print("=== Example Complete ===")

if __name__ == "__main__":
    main() 