"""
Custom Matroid Functions Package

This package contains custom implementations of matroid functions that extend
or fix functionality not available in the standard SageMath matroids module.

Main modules:
- core: Core utility functions and polynomial computations
- polynomials: Polynomial-specific functions for characteristic, KL, and Q polynomials
- chow_polynomials: Chow polynomial computations essential for Poincaré polynomial research
- extensions: Extended functionality for matroid operations
"""

from .core import cmp_elements_key, characteristic_polynomial, whitney_numbers
from .polynomials import (
    uniformQpoly, uniformKLpoly, inverse_kazhdan_lustig_polynomial, invkl,
    kazhdan_lusztig_inverse_uniform, kl_inverse_paving, kl_inverse_copaving
)
from .chow_polynomials import (
    chow_polynomial, get_chow_polynomial, reduced_characteristic_polynomial,
    poincare_polynomial_from_chow, clear_chow_cache, get_chow_cache_info,
    save_chow_cache, export_chow_cache_to_csv
)
from .extensions import is_graphic, is_paving

__all__ = [
    # Core functions
    'cmp_elements_key', 'characteristic_polynomial', 'whitney_numbers',
    
    # Polynomial functions
    'uniformQpoly', 'uniformKLpoly', 'inverse_kazhdan_lustig_polynomial', 'invkl',
    'kazhdan_lusztig_inverse_uniform', 'kl_inverse_paving', 'kl_inverse_copaving',
    
    # Chow polynomial functions
    'chow_polynomial', 'get_chow_polynomial', 'reduced_characteristic_polynomial',
    'poincare_polynomial_from_chow', 'clear_chow_cache', 'get_chow_cache_info',
    'save_chow_cache', 'export_chow_cache_to_csv',
    
    # Extension functions
    'is_graphic', 'is_paving'
] 