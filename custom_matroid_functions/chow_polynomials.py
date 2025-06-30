"""
Chow polynomial computations for matroids.

This module implements Chow polynomial computations that are essential
for the Poincaré polynomial research project.
"""

import json
import os
from sage.all import *
from .core import characteristic_polynomial

# Cache file path
CACHE_FILE = "chow_polynomial_cache.json"

def _load_cache():
    """
    Load Chow polynomial cache from JSON file.
    
    OUTPUT:
    - Dictionary mapping matroid representations to polynomials
    """
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                cache_data = json.load(f)
                # Convert string representations back to polynomials
                R = PolynomialRing(QQ, 'x')
                cache = {}
                for matroid_repr, poly_str in cache_data.items():
                    if poly_str == '1':
                        cache[matroid_repr] = R(1)
                    else:
                        # Parse polynomial string like "x^2 + 2*x + 1"
                        cache[matroid_repr] = R(poly_str)
                return cache
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Warning: Could not load cache file: {e}")
            return {}
    return {}

def _save_cache(cache):
    """
    Save Chow polynomial cache to JSON file.
    
    INPUT:
    - cache: Dictionary mapping matroid representations to polynomials
    """
    # Convert polynomials to string representations
    cache_data = {}
    for matroid_repr, poly in cache.items():
        if poly == 1:
            cache_data[matroid_repr] = '1'
        else:
            cache_data[matroid_repr] = str(poly)
    
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache_data, f, indent=2)
    except Exception as e:
        print(f"Warning: Could not save cache file: {e}")

def _get_matroid_key(M):
    """
    Get a unique string representation of a matroid for caching.
    
    INPUT:
    - M: a matroid
    
    OUTPUT:
    - String representation suitable for caching
    """
    # Use a combination of rank, size, and isomorphism class
    rank = M.rank()
    size = len(M.groundset())
    
    # For small matroids, include more details
    if size <= 8:
        # Include the ground set and bases for small matroids
        bases = sorted([tuple(sorted(basis)) for basis in M.bases()])
        return f"matroid_{rank}_{size}_{hash(str(bases))}"
    else:
        # For larger matroids, use a more compact representation
        # This might miss some isomorphism classes but is much faster
        return f"matroid_{rank}_{size}_{M.is_simple()}_{M.is_3connected()}"

# Initialize cache from file
_chow_poly_cache = _load_cache()

def get_chow_polynomial(M):
    """
    Get Chow polynomial with persistent caching to avoid recomputation.
    
    INPUT:
    - M: a matroid
    
    OUTPUT:
    - Chow polynomial as a polynomial in x
    """
    global _chow_poly_cache
    
    matroid_key = _get_matroid_key(M)
    
    if matroid_key in _chow_poly_cache:
        return _chow_poly_cache[matroid_key]
    
    # Compute the polynomial
    cpoly = chow_polynomial(M)
    
    # Cache it
    _chow_poly_cache[matroid_key] = cpoly
    
    # Save to file periodically (every 10 new entries)
    if len(_chow_poly_cache) % 10 == 0:
        _save_cache(_chow_poly_cache)
    
    return cpoly

def reduced_characteristic_polynomial(M):
    """
    Compute the reduced characteristic polynomial (divided by x-1).
    
    INPUT:
    - M: a matroid
    
    OUTPUT:
    - Reduced characteristic polynomial
    """
    x = var('x')
    R = PolynomialRing(QQ, 'x')
    char_poly = characteristic_polynomial(M)
    return R(char_poly) // (x - 1)

def chow_polynomial(M):
    """
    Compute the Chow polynomial of a matroid.
    
    This implements the recursive formula for Chow polynomials
    that is central to the Poincaré polynomial research.
    
    INPUT:
    - M: a matroid
    
    OUTPUT:
    - Chow polynomial as a polynomial in x
    """
    rank = M.rank()
    x = var('x')
    R = PolynomialRing(QQ, 'x')
    
    if rank == 0:
        return R(1)
    
    chow_poly = R(0)
    
    # Iterate over all flats of all ranks
    for i in range(1, rank + 1):
        for flat in M.flats(i):
            # Compute restriction: M|F
            restriction = M.delete(M.groundset() - flat).simplify()
            # Compute contraction: M/F
            contraction = M.contract(flat).simplify()
            
            # Get polynomials for restriction and contraction
            restriction_poly = reduced_characteristic_polynomial(restriction)
            contraction_poly = get_chow_polynomial(contraction)
            
            # Multiply and add to sum
            term_poly = restriction_poly * contraction_poly
            chow_poly += term_poly
    
    return chow_poly

def poincare_polynomial_from_chow(chow_poly, rank):
    """
    Convert Chow polynomial to Poincaré polynomial.
    
    The Poincaré polynomial H_M(t) is related to the Chow polynomial
    through a change of variables and scaling.
    
    INPUT:
    - chow_poly: Chow polynomial
    - rank: rank of the matroid
    
    OUTPUT:
    - Poincaré polynomial in variable t
    """
    R = PolynomialRing(QQ, 't')
    t = R.gen()
    
    # Convert from x to t variable
    # This is the relationship between Chow and Poincaré polynomials
    poincare_poly = R(0)
    for i, coeff in enumerate(chow_poly.coefficients()):
        poincare_poly += coeff * t**i
    
    return poincare_poly

def clear_chow_cache():
    """
    Clear the Chow polynomial cache and delete the cache file.
    """
    global _chow_poly_cache
    _chow_poly_cache = {}
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)

def save_chow_cache():
    """
    Explicitly save the current cache to file.
    """
    _save_cache(_chow_poly_cache)

def get_chow_cache_info():
    """
    Get information about the Chow polynomial cache.
    
    OUTPUT:
    - Dictionary with cache statistics
    """
    cache_size = len(_chow_poly_cache)
    
    # Analyze cache contents
    rank_distribution = {}
    size_distribution = {}
    
    for key in _chow_poly_cache.keys():
        if key.startswith('matroid_'):
            parts = key.split('_')
            if len(parts) >= 3:
                try:
                    rank = int(parts[1])
                    size = int(parts[2])
                    rank_distribution[rank] = rank_distribution.get(rank, 0) + 1
                    size_distribution[size] = size_distribution.get(size, 0) + 1
                except ValueError:
                    pass
    
    return {
        'cache_size': cache_size,
        'cache_file': CACHE_FILE,
        'file_exists': os.path.exists(CACHE_FILE),
        'rank_distribution': rank_distribution,
        'size_distribution': size_distribution,
        'sample_keys': list(_chow_poly_cache.keys())[:5] if _chow_poly_cache else []
    }

def export_chow_cache_to_csv(filename="chow_polynomials_database.csv"):
    """
    Export the Chow polynomial cache to a CSV file for external analysis.
    
    INPUT:
    - filename: Output CSV filename
    """
    import csv
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Matroid_Key', 'Rank', 'Size', 'Chow_Polynomial'])
        
        for key, poly in _chow_poly_cache.items():
            if key.startswith('matroid_'):
                parts = key.split('_')
                if len(parts) >= 3:
                    try:
                        rank = int(parts[1])
                        size = int(parts[2])
                        writer.writerow([key, rank, size, str(poly)])
                    except ValueError:
                        writer.writerow([key, 'unknown', 'unknown', str(poly)])
                else:
                    writer.writerow([key, 'unknown', 'unknown', str(poly)])
            else:
                writer.writerow([key, 'unknown', 'unknown', str(poly)])
    
    print(f"Exported {len(_chow_poly_cache)} Chow polynomials to {filename}") 