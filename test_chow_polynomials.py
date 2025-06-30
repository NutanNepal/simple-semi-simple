#!/usr/bin/env python3
"""
Test script for Chow polynomial computations.

This script demonstrates how to use the custom Chow polynomial functions
with proper path setup and monkey patching.
"""

import sys
import os

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import SageMath and custom functions
from sage.all import *
from custom_matroid_functions.core import cmp_elements_key
from custom_matroid_functions.chow_polynomials import *

# Apply monkey patch to fix SageMath issues
sage.matroids.utilities.cmp_elements_key = cmp_elements_key

def test_chow_polynomials():
    """Test Chow polynomial computations."""
    
    print("Testing Chow polynomial computations...")
    print("=" * 50)
    
    # Test with uniform matroid U(2,4)
    print("1. Testing with U(2,4):")
    M = matroids.Uniform(2, 4)
    chow_poly = get_chow_polynomial(M)
    print(f"   Chow polynomial: {chow_poly}")
    
    # Test with uniform matroid U(3,6)
    print("\n2. Testing with U(3,6):")
    M2 = matroids.Uniform(3, 6)
    chow_poly2 = get_chow_polynomial(M2)
    print(f"   Chow polynomial: {chow_poly2}")
    
    # Test characteristic polynomial computation
    print("\n3. Testing characteristic polynomial:")
    char_poly = characteristic_polynomial_from_tutte(M)
    print(f"   Characteristic polynomial: {char_poly}")
    
    # Test reduced characteristic polynomial
    print("\n4. Testing reduced characteristic polynomial:")
    red_char_poly = reduced_characteristic_polynomial(M)
    print(f"   Reduced characteristic polynomial: {red_char_poly}")
    
    # Test Poincaré polynomial conversion
    print("\n5. Testing Poincaré polynomial conversion:")
    poincare_poly = poincare_polynomial_from_chow(chow_poly, M.rank())
    print(f"   Poincaré polynomial: {poincare_poly}")
    
    # Show cache information
    print("\n6. Cache information:")
    cache_info = get_chow_cache_info()
    print(f"   Cache size: {cache_info['cache_size']}")
    print(f"   Cached matroids: {cache_info['cached_matroids']}")
    
    print("\n" + "=" * 50)
    print("✅ All tests completed successfully!")

def test_larger_matroid():
    """Test with a larger matroid to show performance."""
    
    print("\nTesting with larger matroid U(4,8):")
    print("=" * 50)
    
    M = matroids.Uniform(4, 8)
    print(f"Matroid: {M}")
    print(f"Rank: {M.rank()}, Size: {M.size()}")
    
    # Time the computation
    import time
    start_time = time.time()
    
    chow_poly = get_chow_polynomial(M)
    
    end_time = time.time()
    computation_time = end_time - start_time
    
    print(f"Chow polynomial: {chow_poly}")
    print(f"Computation time: {computation_time:.2f} seconds")
    
    # Show cache info
    cache_info = get_chow_cache_info()
    print(f"Total cached matroids: {cache_info['cache_size']}")

if __name__ == "__main__":
    test_chow_polynomials()
    test_larger_matroid() 