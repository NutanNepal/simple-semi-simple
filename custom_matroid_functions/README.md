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
- `uniformQpoly(r, n)` - Q-polynomial for uniform matroid U(r,n)
- `uniformKLpoly(r, n)` - Kazhdan-Lusztig polynomial for uniform matroid U(r,n)
- `kazhdan_lusztig_inverse_uniform(k, n)` - Inverse KL polynomial for uniform matroid
- `kl_inverse_fast(M)` - Fast inverse KL polynomial computation
- `kl_inverse_paving(M)` - Inverse KL polynomial for paving matroids
- `kl_inverse_copaving(M)` - Inverse KL polynomial for copaving matroids

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
Q = uniformQpoly(2, 4)
print(f"Q-polynomial: {Q}")

# Check if matroid is graphic
is_g = is_graphic(M)
print(f"Is graphic: {is_g}")

# Fast inverse KL polynomial computation
ikl = kl_inverse_fast(M)
print(f"Inverse KL polynomial: {ikl}")
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