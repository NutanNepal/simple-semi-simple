# SageMath Matroid Functions Reference

Based on the [SageMath Matroid Theory documentation](https://doc.sagemath.org/html/en/reference/matroids/index.html), this file provides a comprehensive list of all available matroid functions and classes.

## Table of Contents

1. [Basics](#basics)
2. [Database of Matroids](#database-of-matroids)
3. [Concrete Implementations](#concrete-implementations)
4. [Chow Rings of Matroids](#chow-rings-of-matroids)
5. [Abstract Matroid Classes](#abstract-matroid-classes)
6. [Advanced Functionality](#advanced-functionality)
7. [Internals](#internals)

## Basics

### Matroid Construction
- Core functions for creating matroids from various inputs
- Abstract matroid class definitions

### The Abstract Matroid Class
- Base class for all matroid implementations
- Common methods and properties shared across matroid types

## Database of Matroids

### Catalog of Matroids
- Pre-defined famous matroids available in SageMath
- Examples: Fano matroid, Pappus matroid, etc.

### Collections of Matroids
- Grouped sets of related matroids
- Systematic collections for testing and examples

### Database of Matroids
- Access to external matroid databases
- Large collections of known matroids

## Concrete Implementations

### Basis Matroids
- Matroids defined by their bases
- Functions for basis manipulation and properties

### Circuit Closures Matroids
- Matroids defined by circuit-closure axioms
- Circuit and closure operations

### Circuits Matroids
- Matroids defined by their circuits
- Circuit enumeration and properties

### Flats Matroids
- Matroids defined by their flats
- Lattice of flats operations

### Gammoids
- Matroids arising from directed graphs
- Graph-theoretic matroid constructions

### Graphic Matroids
- Matroids from undirected graphs
- Graph-to-matroid conversions

### Linear Matroids
- Matroids representable over fields
- Matrix representations and operations

### Rank Function Matroids
- Matroids defined by rank functions
- Rank-based constructions and properties

### Transversal Matroids
- Matroids from set systems
- Matching and transversal properties

## Chow Rings of Matroids

### Chow Ring Ideals of Matroids
- Functions for computing Chow ring ideals
- Ideal generators and relations

### Chow Rings of Matroids
- Complete Chow ring computations
- Ring structure and properties

## Abstract Matroid Classes

### Basis Exchange Matroids
- Matroids satisfying basis exchange axioms
- Basis exchange algorithms

### Dual Matroids
- Dual matroid constructions
- Duality operations and properties

### Minors of Matroids
- Deletion and contraction operations
- Minor computations and properties

## Advanced Functionality

### Advanced Matroid Functionality
- Specialized algorithms and methods
- Advanced computational tools

### Iterators for Linear Subclasses
- Iterators for linear matroid subclasses
- Efficient enumeration methods

### Some Useful Functions for the Matroid Class
- Utility functions for matroid operations
- Helper methods and shortcuts

## Internals

### Lean Matrices
- Internal matrix representations
- Optimized data structures

### Helper Functions for Plotting
- Geometric representation plotting
- Visualization tools for matroids

### Set Systems
- Internal set system implementations
- Set-theoretic operations

### Unpickling Methods
- Serialization and deserialization
- Data persistence methods

## Common SageMath Matroid Functions

### Construction Functions
```python
# Basic matroid construction
matroids.Uniform(r, n)           # Uniform matroid U(r,n)
matroids.catalog.Fano()          # Fano matroid
matroids.Whirl(n)                # Whirl matroid
matroids.Wheel(n)                # Wheel matroid
matroids.CompleteGraphic(n)      # Complete graphic matroid
matroids.CompleteGraphic(n, field) # Over specific field

# From graphs
matroids.Graphic(graph)          # Graphic matroid from graph
matroids.CompleteGraphic(n)      # Complete graph matroid

# From matrices
matroids.Linear(matrix, field)   # Linear matroid from matrix
matroids.VectorMatroid(vectors)  # Vector matroid from vectors

# From circuits/bases/flats
matroids.CircuitClosures(circuits) # From circuit-closure data
matroids.Bases(bases)            # From basis list
matroids.Flats(flats)            # From flats list
```

### Properties and Methods
```python
# Basic properties
M.rank()                         # Rank of matroid
M.size()                         # Size of ground set
M.is_connected()                 # Connectivity check
M.is_simple()                    # Simplicity check
M.is_loopless()                  # Looplessness check

# Operations
M.delete(element)                # Deletion
M.contract(element)              # Contraction
M.minor(X, Y)                    # Minor (delete X, contract Y)
M.dual()                         # Dual matroid

# Lattice operations
M.lattice_of_flats()             # Lattice of flats
M.flats(r)                       # Flats of rank r
M.closure(X)                     # Closure of set X
M.rank(X)                        # Rank of set X

# Circuits and bases
M.circuits()                     # All circuits
M.bases()                        # All bases
M.independent_sets()             # All independent sets
M.dependent_sets()               # All dependent sets

# Polynomials
M.characteristic_polynomial()    # Characteristic polynomial
M.tutte_polynomial()             # Tutte polynomial
M.flow_polynomial()              # Flow polynomial
M.chromatic_polynomial()         # Chromatic polynomial (if graphic)

# Chow ring (if available)
M.chow_ring()                    # Chow ring computation
M.chow_ring_ideal()              # Chow ring ideal
```

### Testing and Examples
```python
# Test if properties hold
M.is_isomorphic(other)           # Isomorphism test
M.is_isomorphic(other, certificate=True) # With certificate

# Examples and catalog
matroids.catalog.Fano()          # Fano matroid
matroids.catalog.Pappus()        # Pappus matroid
matroids.catalog.NonPappus()     # Non-Pappus matroid
matroids.catalog.NonFano()       # Non-Fano matroid
matroids.catalog.AG23()          # AG(2,3)
matroids.catalog.AG32()          # AG(3,2)
matroids.catalog.Terrahawk()     # Terrahawk matroid
matroids.catalog.R10()           # R10 matroid
matroids.catalog.R12()           # R12 matroid
```

## Usage Examples

### Basic Construction
```python
from sage.all import *

# Create a uniform matroid
U24 = matroids.Uniform(2, 4)
print(f"U(2,4) has rank {U24.rank()} and size {U24.size()}")

# Create Fano matroid
F = matroids.catalog.Fano()
print(f"Fano matroid is representable over GF(2): {F.is_field_representable(GF(2))}")

# Create from graph
G = graphs.CompleteGraph(4)
M = matroids.Graphic(G)
print(f"Complete graph K4 has {len(M.bases())} bases")
```

### Chow Ring Computation
```python
# Compute Chow ring (if available)
M = matroids.Uniform(2, 4)
try:
    chow_ring = M.chow_ring()
    print(f"Chow ring: {chow_ring}")
except AttributeError:
    print("Chow ring computation not available for this matroid")
```

### Polynomial Computations
```python
# Characteristic polynomial
M = matroids.catalog.Fano()
chi = M.characteristic_polynomial()
print(f"Characteristic polynomial: {chi}")

# Tutte polynomial
tutte = M.tutte_polynomial()
print(f"Tutte polynomial: {tutte}")
```

## Notes

- Not all matroids support all operations
- Chow ring computations may not be available for all matroid types
- Some functions require specific field representations
- Performance varies significantly between different matroid types
- The SageMath matroid implementation is actively developed

## References

- [SageMath Matroid Theory Documentation](https://doc.sagemath.org/html/en/reference/matroids/index.html)
- SageMath version 10.6 Reference Manual
- Matroid Theory by James Oxley (for theoretical background) 