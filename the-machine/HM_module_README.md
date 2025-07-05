# HM Module Documentation

The `HM_module.py` provides a Python module for working with deformed Möbius algebras in the context of matroid Chow rings and Poincaré polynomial research.

## Overview

This module implements:
- **DeformedMoebiusAlgebra**: A quantum Möbius algebra with custom bases
- **ChowBasis**: A basis adapted for Chow ring computations
- **ZetaBasis**: The classical zeta basis for quantum Möbius algebras
- Utility functions for creating algebras from matroids or lattices

## Installation

Place the `HM_module.py` file in your project directory and ensure the path to your custom matroid functions is accessible.

## Usage

### Basic Import

```python
import sys
sys.path.insert(0, '/path/to/your/project/the-machine')
from HM_module import *
```

### Creating an Algebra

```python
# From a matroid
M = matroids.Uniform(2, 4)
algebra = create_deformed_algebra(M)

# From a lattice of flats
L = M.lattice_of_flats()
algebra = create_deformed_algebra_from_lattice(L)

# With custom base ring
P = LaurentPolynomialRing(QQ, 'x')
algebra = create_deformed_algebra(M, base_ring=P)
```

### Accessing Bases

```python
# Get the different bases
C = algebra.C()      # Chow basis
Z = algebra.zeta()   # Zeta basis
E = algebra.natural() # Natural basis

# Get basis elements
C_basis = C.basis()
Z_basis = Z.basis()
E_basis = E.basis()
```

### Basis Conversions

```python
# Convert between bases
F = frozenset([0, 1])
chow_element = C[F]
natural_element = E(chow_element)  # Convert to natural basis
zeta_element = Z(chow_element)     # Convert to zeta basis
```

## Classes

### DeformedMoebiusAlgebra

Main algebra class that extends SageMath's `QuantumMoebiusAlgebra`.

**Methods:**
- `C()`: Returns the Chow basis
- `zeta()`: Returns the zeta basis
- `natural()`: Returns the natural basis

### ChowBasis

Custom basis for Chow ring computations.

**Features:**
- Indexed by flats of the matroid
- Implements change-of-basis morphism to natural basis
- Uses Poincaré polynomials of minors for basis construction

### ZetaBasis

Classical zeta basis for quantum Möbius algebras.

**Features:**
- Indexed by flats of the matroid
- Implements change-of-basis morphism using Kazhdan-Lusztig polynomials

## Dependencies

- SageMath (for matroid functionality)
- `custom_matroid_functions` package (for Poincaré polynomial computations)
- `sage.combinat.posets.moebius_algebra` (for base algebra functionality)

## Example

See `example_usage.sage` for a complete working example.

## Notes

- The module automatically handles base ring coercion between different polynomial rings
- All bases are indexed by the flats of the underlying matroid
- The Chow basis uses Poincaré polynomials of minors, which are computed using the custom matroid functions package 