# Custom Matroid Functions

This package contains custom implementations of matroid functions that extend or fix functionality not available in the standard SageMath matroids module.

## Installation

Simply place this folder in your project directory. The package can be imported directly:

```python
from custom_matroid_functions import *
```

## Modules

### core.py
Core utility functions and polynomial computations:
- `cmp_elements_key(x)` - Compare elements (integers/strings)
- `characteristic_polynomial(M, la=None)` - Fixed characteristic polynomial computation
- `whitney_numbers(M)` - Whitney numbers of the second kind
- `no_broken_circuits_sets_iterator(M, ordering=None)` - Iterator for no broken circuits sets

### polynomials.py
Polynomial-specific functions:
- `inverse_kazhdan_lustig_uniform(r, n)` - Inverse KL polynomial for uniform matroid U(r,n)
- `kazhdan_lustig_uniform(r, n)` - Kazhdan-Lusztig polynomial for uniform matroid U(r,n)
- `kl_inverse_fast(M)` - Fast inverse KL polynomial computation
- `kl_inverse_paving(M)` - Inverse KL polynomial for paving matroids
- `kl_inverse_copaving(M)` - Inverse KL polynomial for copaving matroids

### chow_polynomials.py
Chow polynomial computations essential for Poincaré polynomial research:
- `chow_polynomial(M)` - Compute the Chow polynomial of a matroid
- `get_chow_polynomial(M)` - Get Chow polynomial with persistent caching
- `reduced_characteristic_polynomial(M)` - Compute reduced characteristic polynomial (divided by x-1)
- `poincare_polynomial_of_minor(M, F, G)` - Compute Poincaré polynomial of contraction M/F
- `clear_chow_cache()` - Clear the Chow polynomial cache
- `get_chow_cache_info()` - Get cache statistics
- `save_chow_cache()` - Explicitly save cache to file
- `export_chow_cache_to_csv(filename)` - Export cache to CSV for analysis

### extensions.py
Extended functionality:
- `is_graphic(matroid)` - Check if matroid is graphic using excluded minors
- `is_paving(M)` - Check if matroid is paving

## Usage Examples

```python
# Import the package
from custom_matroid_functions import *

# Create a matroid
M = matroids.Uniform(2, 4)

# Use custom characteristic polynomial (fixes SageMath issues)
chi = characteristic_polynomial(M)
print(f"Characteristic polynomial: {chi}")

# Compute Q-polynomial for uniform matroid
Q = inverse_kazhdan_lustig_uniform(2, 4)
print(f"Q-polynomial: {Q}")

# Check if matroid is graphic
is_g = is_graphic(M)
print(f"Is graphic: {is_g}")

# Fast inverse KL polynomial computation
ikl = kl_inverse_fast(M)
print(f"Inverse KL polynomial: {ikl}")

# Example usage
KL = kazhdan_lustig_uniform(2, 4)
print(f"KL-polynomial: {KL}")

# Chow polynomial computations
chow = get_chow_polynomial(M)
print(f"Chow polynomial: {chow}")

# Poincaré polynomial of a minor
F = frozenset([0, 1])
G = frozenset([2])
poincare = poincare_polynomial_of_minor(M, F, G)
print(f"Poincaré polynomial of minor: {poincare}")
```

## Why Custom Functions?

The standard SageMath matroids module has some limitations:

1. **Characteristic Polynomial Issues**: The built-in `characteristic_polynomial()` function may fail due to `cmp_elements_key` issues
2. **Missing Polynomial Functions**: Some polynomial computations (like Q-polynomials) are not available
3. **Performance**: Custom implementations may be faster for specific cases
4. **Reliability**: Custom implementations may be more reliable for certain matroid types

## Dependencies

- SageMath (for basic matroid functionality)
- All standard SageMath imports (`sage.all`)

## Notes

- This package is designed to work alongside the standard SageMath matroids module
- Functions are organized by functionality for easy maintenance
- All functions include proper documentation and examples
- The package follows Python import conventions 