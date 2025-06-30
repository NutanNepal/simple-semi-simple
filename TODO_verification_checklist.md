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
- [ ] **`uniformQpoly(r, n)`**: Verify against known formulas for U(2,4), U(2,5), U(3,6)
- [ ] Check that Q-polynomials satisfy expected properties (degree, coefficients)

### ✅ Kazhdan-Lusztig Polynomials
- [ ] **`uniformKLpoly(r, n)`**: Verify against known values for small uniform matroids
- [ ] Check that KL polynomials have non-negative coefficients
- [ ] Verify degree bounds (≤ (rank-1)/2)

### ✅ Inverse Kazhdan-Lusztig Polynomials
- [ ] **`inverse_kazhdan_lustig_polynomial(M)`**: Test with uniform matroids
- [ ] **`invkl` alias**: Verify it works identically to the full function name
- [ ] **`kazhdan_lusztig_inverse_uniform(k, n)`**: Verify against known formulas
- [ ] Test with paving and copaving matroids
- [ ] Verify the inverse relationship: KL(M) * invKL(M) = 1 (mod t^r)

### 🔍 Verification Tests
```python
# Test uniform Q-polynomials
assert uniformQpoly(2, 4) == 1 + 2*t + t^2  # Verify known value

# Test uniform KL polynomials
assert uniformKLpoly(2, 4) == 1 + t  # Verify known value

# Test inverse KL polynomials
M = matroids.Uniform(2, 4)
inv_poly = inverse_kazhdan_lustig_polynomial(M)
assert inv_poly == invkl(M)  # Test alias
```

---

## 3. Chow Polynomial Functions (`custom_matroid_functions/chow_polynomials.py`)

### ✅ Core Functions
- [ ] **`chow_polynomial(M)`**: Test with small matroids (rank ≤ 3)
- [ ] **`get_chow_polynomial(M)`**: Verify caching works correctly
- [ ] **`reduced_characteristic_polynomial(M)`**: Test division by (x-1)
- [ ] **`poincare_polynomial_from_chow(chow_poly, rank)`**: Verify variable change

### ✅ Cache System
- [ ] **Persistent JSON cache**: Test that cache file is created and loaded
- [ ] **Cache performance**: Verify significant speedup on repeated computations
- [ ] **Cache management**: Test `clear_chow_cache()`, `save_chow_cache()`
- [ ] **Cache statistics**: Test `get_chow_cache_info()`
- [ ] **CSV export**: Test `export_chow_cache_to_csv()`

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
- [ ] **Function aliases**: Verify `invkl` works as expected

### 🔍 Verification Tests
```python
# Test package imports
from custom_matroid_functions import *
assert 'inverse_kazhdan_lustig_polynomial' in dir()
assert 'invkl' in dir()
assert invkl == inverse_kazhdan_lustig_polynomial
```

---

## 6. Mathematical Definitions (`definitions/`)

### ✅ Definition Files
- [ ] **`mathematical_objects.md`**: Review all definitions for accuracy
- [ ] **`computational_framework.md`**: Verify implementation goals match functions
- [ ] Check that definitions align with source papers (BV, BHMPW, ANR)

### 🔍 Verification Tasks
- [ ] Cross-reference definitions with source papers
- [ ] Verify Chow ring definitions match BHMPW paper
- [ ] Check FY basis definitions match ANR paper
- [ ] Verify deletion homomorphism definition matches BV paper

---

## 7. Test Scripts and Examples

### ✅ Test Files
- [ ] **`test_persistent_cache.py`**: Run and verify all tests pass
- [ ] **`test_chow_polynomials.py`**: Run and verify Chow polynomial tests
- [ ] Create additional tests for edge cases

### 🔍 Verification Tests
```bash
# Run test scripts
sage -python test_persistent_cache.py
sage -python test_chow_polynomials.py
```

---

## 8. File Organization and Git

### ✅ Project Structure
- [ ] **`.gitignore`**: Verify cache files are properly excluded
- [ ] **File organization**: Check that all files are in correct locations
- [ ] **Documentation**: Verify README files are up to date

### 🔍 Verification Tasks
- [ ] Check that `chow_polynomial_cache.json` is in `.gitignore`
- [ ] Verify `matroids/` folder is excluded from git
- [ ] Test that cache files are created but not committed

---

## 9. Performance and Scalability

### ✅ Performance Tests
- [ ] **Small matroids** (rank ≤ 3, size ≤ 8): Should be fast
- [ ] **Medium matroids** (rank ≤ 5, size ≤ 12): Should complete in reasonable time
- [ ] **Cache performance**: Verify significant speedup on repeated computations
- [ ] **Memory usage**: Check that cache doesn't grow excessively

### 🔍 Verification Tests
```python
# Test performance with different matroid sizes
import time

# Small matroid
M1 = matroids.Uniform(2, 4)
start = time.time()
chow_poly1 = get_chow_polynomial(M1)
time1 = time.time() - start
assert time1 < 1.0  # Should be fast

# Medium matroid
M2 = matroids.Uniform(3, 7)
start = time.time()
chow_poly2 = get_chow_polynomial(M2)
time2 = time.time() - start
assert time2 < 10.0  # Should complete in reasonable time
```

---

## 10. Mathematical Correctness

### ✅ Core Mathematical Properties
- [ ] **Chow polynomials**: Verify they satisfy expected properties
- [ ] **Poincaré duality**: Test that H_M(t) = t^(d-1) * H_M(t^(-1))
- [ ] **Recursive formulas**: Verify deletion-contraction relations
- [ ] **Polynomial degrees**: Check degree bounds are satisfied

### 🔍 Verification Tests
```python
# Test Poincaré duality for small matroids
M = matroids.Uniform(2, 4)
chow_poly = chow_polynomial(M)
poincare_poly = poincare_polynomial_from_chow(chow_poly, M.rank())

# Check Poincaré duality
t = poincare_poly.parent().gen()
d = M.rank()
assert poincare_poly == t^(d-1) * poincare_poly.subs(t=1/t)
```

---

## 11. Integration with Research Goals

### ✅ Research Alignment
- [ ] **BV framework adaptation**: Verify functions support the algebraic framework
- [ ] **Poincaré polynomial goal**: Check that functions enable the main research objective
- [ ] **Computational experiments**: Ensure functions support planned experiments

### 🔍 Verification Tasks
- [ ] Test that `H(M)` module structure can be implemented
- [ ] Verify deletion homomorphism can be computed
- [ ] Check that perverse elements can be identified
- [ ] Test Chow-Poincaré element construction

---

## 12. Documentation and Examples

### ✅ Documentation
- [ ] **Function docstrings**: Verify all functions have clear documentation
- [ ] **Usage examples**: Add examples for complex functions
- [ ] **Mathematical context**: Ensure documentation references source papers

### 🔍 Verification Tasks
- [ ] Review all function docstrings for clarity
- [ ] Add usage examples for complex functions
- [ ] Cross-reference with source papers

---

## Priority Levels

### 🔴 **High Priority** (Must verify before proceeding)
1. Core mathematical correctness (Section 10)
2. Basic function functionality (Sections 1-4)
3. Package imports and structure (Section 5)

### 🟡 **Medium Priority** (Should verify soon)
4. Performance and scalability (Section 9)
5. Cache system functionality (Section 3)
6. Test script execution (Section 7)

### 🟢 **Low Priority** (Can verify later)
7. Documentation completeness (Section 12)
8. File organization (Section 8)
9. Integration with research goals (Section 11)

---

## Next Steps After Verification

Once you've completed the high-priority verifications:

1. **Run comprehensive tests** on a variety of matroids
2. **Document any issues** found during verification
3. **Create additional test cases** for edge cases
4. **Plan computational experiments** for the research project
5. **Begin implementing the BV framework adaptation**

---

## Notes

- **Focus on mathematical correctness first** - this is the foundation of your research
- **Test with small, known examples** before moving to larger matroids
- **Keep the cache system** - it will be essential for larger computations
- **Document any discrepancies** between your implementations and expected results

This verification process will ensure that your computational framework is solid before you begin the main research work on the Poincaré polynomial proof. 