# TODO: Verification Checklist

## Overview
This checklist covers all the components we've created and modified for the matroid research project. Please verify each item before proceeding with further development.

---

## 1. Core Matroid Functions (`custom_matroid_functions/core.py`)

### ✅ Basic Functions
- [ ] **`cmp_elements_key`**: Test with various matroids to ensure consistent element ordering
- [ ] **`characteristic_polynomial`**: Verify against SageMath's built-in function for small matroids
- [ ] **`whitney_numbers`**: Test with known examples (uniform matroids, graphic matroids)

### 🔍 Verification Tests
```python
# Test characteristic polynomial
M = matroids.Uniform(2, 4)
assert characteristic_polynomial(M) == M.characteristic_polynomial()

# Test whitney numbers
M = matroids.Uniform(2, 4)
w = whitney_numbers(M)
assert len(w) == M.rank() + 1
```

---

## 2. Polynomial Functions (`custom_matroid_functions/polynomials.py`)

### ✅ Q-Polynomials
- [ ] Check that Q-polynomials satisfy expected properties (degree, coefficients)

### ✅ Kazhdan-Lusztig Polynomials
- [x] **`kazhdan_lustig_uniform(r, n)`**: Verified against known values for small uniform matroids
- [x] Check that KL polynomials have non-negative coefficients
- [x] Verify degree bounds (≤ (rank-1)/2)

### ✅ Inverse Kazhdan-Lusztig Polynomials
- [x] **`inverse_kazhdan_lustig_uniform(r, n)`**: Verified against known formulas for U(2,4), U(2,5), U(3,6)
- [x] Test with paving and copaving matroids
- [x] Verify the inverse relationship: KL(M) * invKL(M) = 1 (mod t^r)

### 🔍 Verification Tests
```python
# Test uniform Q-polynomials
assert kazhdan_lustig_uniform(2, 4) == 1 + t  # Verify known value

# Test uniform KL polynomials
assert kazhdan_lustig_uniform(2, 4) == 1 + t  # Verify known value

# Test inverse KL polynomials
M = matroids.Uniform(2, 4)
inv_poly = inverse_kazhdan_lustig_polynomial(M)
assert inv_poly == invkl(M)  # Test alias
```

---

## 3. Chow Polynomial Functions (`custom_matroid_functions/chow_polynomials.py`)

### ✅ Core Functions
- [x] **`chow_polynomial(M)`**: Verified for small matroids
- [x] **`get_chow_polynomial(M)`**: Verified for small matroids
- [x] **`reduced_characteristic_polynomial(M)`**: Test division by (x-1)
- [x] **`poincare_polynomial_from_chow(chow_poly, rank)`**: Verify variable change

### ✅ Cache System
- [x] **Persistent JSON cache**: Test that cache file is created and loaded
- [x] **Cache performance**: Verify significant speedup on repeated computations
- [x] **Cache management**: Test `clear_chow_cache()`, `save_chow_cache()`
- [x] **Cache statistics**: Test `get_chow_cache_info()`
- [x] **CSV export**: Test `export_chow_cache_to_csv()`

### 🔍 Verification Tests
```python
# Test Chow polynomial computation
M = matroids.Uniform(2, 4)
chow_poly = chow_polynomial(M)
assert chow_poly.degree() <= M.rank()

# Test caching
chow_poly1 = get_chow_polynomial(M)
chow_poly2 = get_chow_polynomial(M)  # Should use cache
assert chow_poly1 == chow_poly2

# Test cache persistence
save_chow_cache()
info = get_chow_cache_info()
assert info['cache_size'] > 0
```

### ✅ Documentation and Examples
- [x] All function docstrings reviewed for clarity
- [x] Usage examples for custom functions updated

---

## 4. Extension Functions (`custom_matroid_functions/extensions.py`)

### ✅ Matroid Properties
- [ ] **`is_graphic(M)`**: Test with known graphic and non-graphic matroids
- [ ] **`is_paving(M)`**: Test with paving and non-paving matroids
- [ ] Verify these functions give correct results for small examples

### 🔍 Verification Tests
```python
# Test graphic matroid detection
K4 = matroids.CompleteGraphic(4)
assert is_graphic(K4) == True

# Test paving matroid detection
U24 = matroids.Uniform(2, 4)
assert is_paving(U24) == True
```

---

## 5. Package Structure and Imports

### ✅ Package Initialization
- [ ] **`__init__.py`**: Verify all functions are properly exported
- [ ] **Import statements**: Test `from custom_matroid_functions import *`
- [ ] **Function aliases**: Verify `invkl`

### ✅ Custom Function Refactor and Cache
- [x] All custom function renaming (KL, inverse KL, Chow) completed
- [x] All references to old function names updated
- [x] Persistent cache implemented for KL, inverse KL, and Chow polynomials
- [x] All caches save after every new entry
- [x] Custom function documentation and usage examples updated
- [x] All user-facing custom functions reviewed and verified

---

## 6. HM Module Development (`the-machine/HM_module.py`)

### ✅ Core Algebra Classes
- [x] **`DeformedMoebiusAlgebra`**: Implemented with base ring support
- [x] **`ChowBasis`**: Implemented with proper change-of-basis morphism
- [x] **`ZetaBasis`**: Implemented with Kazhdan-Lusztig polynomial basis
- [x] Base ring coercion fixed (ZZ vs QQ polynomial rings)

### ✅ Module Structure
- [x] **Module accessibility**: Can be imported from other files
- [x] **Utility functions**: `create_deformed_algebra()`, `create_deformed_algebra_from_lattice()`
- [x] **Proper imports**: Added missing `Matroid` constructor import
- [x] **`__all__` list**: Controls what gets imported with `from HM_module import *`

### ✅ Documentation and Examples
- [x] **`HM_module_README.md`**: Comprehensive documentation created
- [x] **`example_usage.sage`**: Working example file demonstrating all functionality
- [x] **Usage examples**: Basis conversions, algebra creation, basis access

### 🔍 Verification Tests
```python
# Test module import
import sys
sys.path.insert(0, '/home/nnutannep/Github/simple-semi-simple/the-machine')
from HM_module import *

# Test algebra creation
M = matroids.Uniform(2, 4)
algebra = create_deformed_algebra(M)
assert isinstance(algebra, DeformedMoebiusAlgebra)

# Test basis access
C = algebra.C()
Z = algebra.zeta()
E = algebra.natural()
assert C is not None and Z is not None and E is not None

# Test basis conversions
F = frozenset([0, 1])
if F in C.basis():
    chow_element = C[F]
    natural_element = E(chow_element)
    zeta_element = Z(chow_element)
    assert natural_element is not None and zeta_element is not None
```

---

## 7. Recent Fixes and Improvements

### ✅ Base Ring Issues
- [x] **Fixed base ring mismatch**: ZZ vs QQ polynomial rings
- [x] **Added coercion**: Polynomials properly coerced to algebra's base ring
- [x] **Fixed `poincare_polynomial_of_minor`**: Now accepts both matroids and algebras
- [x] **Fixed `ChowBasis._to_natural_basis`**: Proper matroid extraction and polynomial coercion

### ✅ Function Updates
- [x] **`poincare_polynomial_of_minor`**: Added to custom_matroid_functions package
- [x] **Updated imports**: Added to `__init__.py` and `__all__` list
- [x] **Updated documentation**: Added to README with usage examples