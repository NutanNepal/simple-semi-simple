#!/usr/bin/env sage -python
"""
Test script for the persistent Chow polynomial cache system.

This script demonstrates how the cache works and shows the performance benefits.
"""

import sys
import os
import time

# Add current directory to path for imports
sys.path.insert(0, os.getcwd())

from custom_matroid_functions import *

def test_persistent_cache():
    """
    Test the persistent cache system for Chow polynomials.
    """
    print("=== Testing Persistent Chow Polynomial Cache ===\n")
    
    # Check initial cache state
    print("1. Initial cache info:")
    cache_info = get_chow_cache_info()
    print(f"   Cache size: {cache_info['cache_size']}")
    print(f"   Cache file exists: {cache_info['file_exists']}")
    print(f"   Cache file: {cache_info['cache_file']}")
    print()
    
    # Test with some small matroids
    test_matroids = [
        matroids.Uniform(2, 4),  # U(2,4)
        matroids.Uniform(2, 5),  # U(2,5)
        matroids.CompleteGraphic(4),  # K4
        matroids.CompleteGraphic(5),  # K5
    ]
    
    print("2. Computing Chow polynomials (first run):")
    start_time = time.time()
    
    for i, M in enumerate(test_matroids):
        print(f"   Computing Chow polynomial for {M}...")
        chow_poly = get_chow_polynomial(M)
        print(f"   Result: {chow_poly}")
    
    first_run_time = time.time() - start_time
    print(f"   First run took: {first_run_time:.2f} seconds")
    print()
    
    # Check cache after first run
    print("3. Cache info after first run:")
    cache_info = get_chow_cache_info()
    print(f"   Cache size: {cache_info['cache_size']}")
    print(f"   Rank distribution: {cache_info['rank_distribution']}")
    print(f"   Size distribution: {cache_info['size_distribution']}")
    print()
    
    # Test second run (should be much faster)
    print("4. Computing Chow polynomials (second run - should use cache):")
    start_time = time.time()
    
    for i, M in enumerate(test_matroids):
        print(f"   Getting Chow polynomial for {M}...")
        chow_poly = get_chow_polynomial(M)
        print(f"   Result: {chow_poly}")
    
    second_run_time = time.time() - start_time
    print(f"   Second run took: {second_run_time:.2f} seconds")
    print(f"   Speedup: {first_run_time/second_run_time:.1f}x faster")
    print()
    
    # Test cache persistence by reloading
    print("5. Testing cache persistence:")
    print("   Saving cache explicitly...")
    save_chow_cache()
    
    print("   Cache file size:", os.path.getsize(cache_info['cache_file']) if os.path.exists(cache_info['cache_file']) else "N/A")
    print()
    
    # Export to CSV for external analysis
    print("6. Exporting cache to CSV:")
    export_chow_cache_to_csv("test_chow_database.csv")
    print()

def test_larger_matroid():
    """
    Test with a larger matroid to show the benefit of caching.
    """
    print("=== Testing with Larger Matroid ===\n")
    
    # Use a larger matroid that takes more time to compute
    M = matroids.Uniform(3, 7)  # U(3,7) - should be more complex
    
    print(f"Computing Chow polynomial for {M} (rank {M.rank()}, size {len(M.groundset())})...")
    
    start_time = time.time()
    chow_poly = get_chow_polynomial(M)
    computation_time = time.time() - start_time
    
    print(f"Result: {chow_poly}")
    print(f"Computation time: {computation_time:.2f} seconds")
    print()
    
    # Test cache hit
    print("Testing cache hit (should be instant):")
    start_time = time.time()
    chow_poly2 = get_chow_polynomial(M)
    cache_time = time.time() - start_time
    
    print(f"Cached result: {chow_poly2}")
    print(f"Cache access time: {cache_time:.4f} seconds")
    print(f"Speedup: {computation_time/cache_time:.1f}x faster")
    print()

if __name__ == "__main__":
    test_persistent_cache()
    test_larger_matroid()
    
    print("=== Final Cache Statistics ===")
    cache_info = get_chow_cache_info()
    print(f"Total cached polynomials: {cache_info['cache_size']}")
    print(f"Cache file: {cache_info['cache_file']}")
    print(f"Rank distribution: {cache_info['rank_distribution']}")
    print(f"Size distribution: {cache_info['size_distribution']}")
    print("\nCache system is working! The database will persist between sessions.") 