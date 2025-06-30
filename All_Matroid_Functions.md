# All Matroid Functions - Complete Reference

This file lists ALL functions available in the SageMath matroids module, organized by category and source file.

---

## 1. Main Matroid Class Methods (from matroid.pxd)

### Core Properties and Oracle Methods
- `groundset()`
- `size()`
- `rank(X=*)`
- `full_rank()`
- `basis()`
- `max_independent(X)`
- `circuit(X=*)`
- `fundamental_circuit(B, e)`
- `closure(X)`
- `k_closure(X, k)`
- `augment(X, Y=*)`
- `corank(X=*)`
- `full_corank()`
- `cobasis()`
- `max_coindependent(X)`
- `cocircuit(X=*)`
- `fundamental_cocircuit(B, e)`
- `coclosure(X)`

### Independence and Basis Testing
- `loops()`
- `is_independent(X)`
- `is_dependent(X)`
- `is_basis(X)`
- `is_circuit(X)`
- `is_closed(X)`
- `is_subset_k_closed(X, k)`
- `coloops()`
- `is_coindependent(X)`
- `is_codependent(X)`
- `is_cobasis(X)`
- `is_cocircuit(X)`
- `is_coclosed(X)`
- `is_valid()`

### Enumeration
- `circuits(k=*)`
- `nonspanning_circuits()`
- `cocircuits()`
- `noncospanning_cocircuits()`
- `circuit_closures()`
- `nonspanning_circuit_closures()`
- `bases()`
- `independent_sets(k=*)`
- `nonbases()`
- `dependent_sets(k)`
- `flats(k)`
- `coflats(k)`
- `hyperplanes()`
- `f_vector()`
- `whitney_numbers()`
- `whitney_numbers2()`
- `broken_circuits(ordering=*)`
- `no_broken_circuits_sets(ordering=*)`

### Polytopes
- `matroid_polytope()`
- `independence_matroid_polytope()`

### Isomorphism and Equality
- `is_isomorphic(other, certificate=*)`
- `isomorphism(other)`
- `equals(other)`
- `is_isomorphism(other, morphism)`

### Minors, Dual, Truncation
- `minor(contractions=*, deletions=*)`
- `contract(X)`
- `delete(X)`
- `dual()`
- `truncation()`
- `has_minor(N, certificate=*)`
- `has_line_minor(k, hyperlines=*, certificate=*)`

### Extension and Coextension
- `extension(element=*, subsets=*)`
- `coextension(element=*, subsets=*)`
- `modular_cut(subsets)`
- `linear_subclasses(line_length=*, subsets=*)`
- `extensions(element=*, line_length=*, subsets=*)`
- `coextensions(element=*, coline_length=*, subsets=*)`

### Connectivity and Simplification
- `simplify()`
- `cosimplify()`
- `is_simple()`
- `is_cosimple()`
- `components()`
- `is_connected(certificate=*)`
- `connectivity(S, T=*)`
- `is_kconnected(k, certificate=*)`
- `link(S, T)`
- `is_3connected(certificate=*, algorithm=*)`
- `is_4connected(certificate=*, algorithm=*)`
- `is_paving()`
- `is_sparse_paving()`
- `girth()`

### Representability
- `binary_matroid(randomized_tests=*, verify=*)`
- `is_binary(randomized_tests=*)`
- `ternary_matroid(randomized_tests=*, verify=*)`
- `is_ternary(randomized_tests=*)`
- `is_regular()`
- `is_graphic()`

### Chordality and k-closed
- `is_k_closed(k)`
- `is_circuit_chordal(C, certificate=*)`
- `is_chordal(k1=*, k2=*, certificate=*)`
- `chordality()`

### Optimization
- `max_weight_independent(X=*, weights=*)`
- `max_weight_coindependent(X=*, weights=*)`
- `is_max_weight_independent_generic(X=*, weights=*)`
- `is_max_weight_coindependent_generic(X=*, weights=*)`
- `intersection(other, weights=*)`
- `intersection_unweighted(other)`
- `partition()`

### Invariants and Polynomials
- `tutte_polynomial(x=*, y=*)`
- `characteristic_polynomial(la=*)`
- `flat_cover(solver=*, verbose=*, integrality_tolerance=*)`

### Miscellaneous
- `automorphism_group()`
- `bergman_complex()`
- `augmented_bergman_complex()`
- `broken_circuit_complex(ordering=*)`
- `plot(B=*, lineorders=*, pos_method=*, pos_dict=*, save_pos=*)`
- `show(B=*, lineorders=*, pos_method=*, pos_dict=*, save_pos=*, lims=*)`
- `direct_sum(matroids)`

---

## 2. Construction Functions (from constructor.py)

### Main Constructor
- `Matroid(groundset=None, data=None, **kwds)` - Main constructor for creating matroids from various inputs

**Supported inputs:**
- `bases` - List of bases
- `independent_sets` - List of independent sets  
- `circuits` - List of circuits
- `nonspanning_circuits` - List of nonspanning circuits
- `flats` - Dictionary/list/lattice of flats
- `graph` - Graph object
- `matrix` - Matrix representation
- `reduced_matrix` - Reduced matrix representation
- `morphism` - Morphism representation
- `reduced_morphism` - Reduced morphism representation
- `rank_function` - Rank function
- `circuit_closures` - Circuit closures
- `revlex` - RevLex encoding string

---

## 3. Utility Functions (from utilities.py)

### Printing and Display
- `setprint(X)` - Print nested data structures nicely
- `setprint_s(X, toplevel=False)` - Create string for setprint

### Labeling
- `newlabel(groundset)` - Create new element label

### Minor Operations
- `sanitize_contractions_deletions(matroid, contractions, deletions)` - Fix contraction/deletion sets

### Matroid Conversion
- `make_regular_matroid_from_matroid(matroid)` - Convert to regular matroid

### Enumeration
- `get_nonisomorphic_matroids(MSet)` - Get non-isomorphic matroids

### Graph Operations
- `spanning_forest(M)` - Find spanning forest
- `spanning_stars(M)` - Find spanning stars
- `split_vertex(G, u, v=None, edges=None)` - Split vertex in graph

### Lifting Operations
- `lift_cross_ratios(A, lift_map=None)` - Lift cross ratios
- `lift_map(target)` - Create lift map

### Comparison
- `cmp_elements_key(x)` - Comparison key for elements

---

## 4. Catalog Functions (from matroids_catalog.py)

### Parametrized Matroids
- `matroids.AG(r, q)` - Affine geometry matroid
- `matroids.CompleteGraphic(n)` - Complete graphic matroid
- `matroids.PG(r, q)` - Projective geometry matroid
- `matroids.Psi(r)` - Psi matroid
- `matroids.Spike(r, F=None, G=None)` - Spike matroid
- `matroids.Theta(r)` - Theta matroid
- `matroids.Uniform(r, n)` - Uniform matroid U(r,n)
- `matroids.Wheel(n)` - Wheel matroid
- `matroids.Whirl(n)` - Whirl matroid
- `matroids.Z(r)` - Z matroid

### Individual Matroids (via matroids.catalog.*)

#### Oxley's Collection
- `U24`, `U25`, `U35`, `K4`, `Whirl3`, `Q6`, `P6`, `U36`, `R6`
- `Fano`, `FanoDual`, `NonFano`, `NonFanoDual`, `O7`, `P7`
- `AG32`, `AG32prime`, `R8`, `F8`, `Q8`, `L8`, `S8`, `Vamos`, `T8`, `J`, `P8`, `P8pp`
- `Wheel4`, `Whirl4`, `K33dual`, `K33`, `AG23`, `TernaryDowling3`, `R9`, `Pappus`, `NonPappus`
- `K5`, `K5dual`, `R10`, `NonDesargues`, `R12`, `ExtendedTernaryGolayCode`, `T12`, `PG23`

#### Brettell's Collection
- `RelaxedNonFano`, `TippedFree3spike`, `AG23minusDY`, `TQ8`, `P8p`, `KP8`, `Sp8`, `Sp8pp`, `LP8`, `WQ8`
- `BB9`, `TQ9`, `TQ9p`, `M8591`, `PP9`, `BB9gDY`, `A9`, `FN9`, `FX9`, `KR9`, `KQ9`
- `UG10`, `FF10`, `GP10`, `FZ10`, `UQ10`, `FP10`, `TQ10`, `FY10`, `PP10`, `FU10`, `D10`, `UK10`
- `PK10`, `GK10`, `FT10`, `TK10`, `KT10`, `TU10`, `UT10`, `FK10`, `KF10`, `FA11`
- `FR12`, `GP12`, `FQ12`, `FF12`, `FZ12`, `UQ12`, `FP12`, `FS12`, `UK12`, `UA12`, `AK12`
- `FK12`, `KB12`, `AF12`, `NestOfTwistedCubes`, `XY13`, `N3`, `N3pp`, `UP14`, `VP14`, `FV14`, `OW14`, `FM14`, `FA15`, `N4`

#### Various Collections
- `NonVamos`, `NotP8`, `AG23minus`, `P9`, `R9A`, `R9B`, `Block_9_4`, `TicTacToe`
- `N1`, `Block_10_5`, `Q10`, `BetsyRoss`, `N2`, `D16`, `Terrahawk`, `ExtendedBinaryGolayCode`

---

## 5. Advanced Functions (from advanced.py)

### Advanced Classes (import with `from sage.matroids.advanced import *`)
- `BasisMatroid` - Matroid defined by bases
- `CircuitsMatroid` - Matroid defined by circuits  
- `CircuitClosuresMatroid` - Matroid defined by circuit closures
- `DualMatroid` - Dual of a matroid
- `FlatsMatroid` - Matroid defined by flats
- `GraphicMatroid` - Graphic matroid
- `LinearMatroid` - Linear matroid
- `RegularMatroid` - Regular matroid
- `BinaryMatroid` - Binary matroid
- `TernaryMatroid` - Ternary matroid
- `QuaternaryMatroid` - Quaternary matroid
- `MinorMatroid` - Minor of a matroid
- `RankMatroid` - Matroid defined by rank function
- `LinearSubclasses` - Linear subclasses
- `MatroidExtensions` - Matroid extensions
- `MatroidUnion` - Union of matroids
- `MatroidSum` - Sum of matroids
- `PartitionMatroid` - Partition matroid

### Advanced Functions
- `setprint()` - Print nested structures nicely
- `newlabel()` - Create new element label
- `get_nonisomorphic_matroids()` - Get non-isomorphic matroids
- `lift_cross_ratios()` - Lift cross ratios
- `lift_map()` - Create lift map
- `cmp_elements_key()` - Comparison key for elements

---

## 6. Database Functions (from database_collections.py)

### Collection Classes
- `AllMatroids` - All matroids in database
- `BrettellMatroids` - Brettell's matroid collection
- `OxleyMatroids` - Oxley's matroid collection  
- `VariousMatroids` - Various matroid collection

---

## 7. Plotting Functions (from matroids_plot_helpers.py)

### Visualization
- `plot()` - Plot matroid
- `show()` - Show matroid plot
- `_fix_positions()` - Fix plot positions

---

## 8. Database Functions (from database_matroids.py)

### All Individual Matroid Constructors
All the individual matroid functions listed in section 4 above are implemented in this file.

---

## Usage Examples

### Basic Construction
```python
# Using main constructor
M = Matroid(bases=[[1,2], [1,3], [2,3]])
M = Matroid(circuits=[[1,2,3]])
M = Matroid(flats={1: [[1]], 2: [[1,2], [1,3], [2,3]], 3: [[1,2,3]]})

# Using catalog
F = matroids.catalog.Fano()
U = matroids.Uniform(2, 4)
W = matroids.Wheel(4)
```

### Advanced Usage
```python
from sage.matroids.advanced import *

# Direct class construction
M = BasisMatroid(bases=[[1,2], [1,3], [2,3]])
M = CircuitsMatroid(circuits=[[1,2,3]])
M = FlatsMatroid(flats={1: [[1]], 2: [[1,2], [1,3], [2,3]], 3: [[1,2,3]]})

# Utility functions
setprint(M.bases())
new_label = newlabel(M.groundset())
```

---

## Notes

- This list covers all functions available in the SageMath matroids module
- Functions are organized by their source file and category
- Some functions may have additional parameters not shown here
- For detailed documentation, use `help(function_name)` in SageMath
- The module is actively developed, so new functions may be added in future versions 