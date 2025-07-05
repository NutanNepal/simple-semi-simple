# Project Context: The Semi-Small Project

## 1. Primary Objective

The core goal of this project is to find a new, elementary, and purely algebraic proof for the formula of the **Poincaré polynomial of a matroid's Chow ring**, denoted `H_M(t)`. The existing proofs, found in the work of Braden, Huh, Matherne, Proudfoot, and Wang (BHMPW), rely on deep and complex geometric machinery (specifically, the semi-small decomposition of the Chow ring). Our aim is to develop a more direct proof by adapting algebraic techniques from related areas of combinatorics.

## 2. Core Hypothesis & Strategy

The central strategy is to **adapt the algebraic framework developed by Braden and Vysogorets (BV) for Kazhdan-Lusztig (KL) polynomials of matroids.**

The BV framework involves:
- An algebraic module, denoted `H(M)`, which is a free module over `Z[t, t⁻¹]` with a basis corresponding to the flats of the matroid `M`.
- A "deletion" homomorphism, `Δ: H(M) -> H(M\e)`, which describes how elements behave upon deleting an element `e` from the matroid's ground set.
- A special class of "perverse" elements in `H(M)` whose structure is key to deriving recursive formulas.

**Our central hypothesis is that a similar structure exists for the Poincaré polynomials.** We will define a "Chow-Poincaré element" in the module `H(M)` and conjecture that it satisfies a key "perversity" condition under the action of the deletion homomorphism `Δ`. Proving this conjecture should lead directly to the desired recursive formula for `H_M(t)`.

## 3. Key Mathematical Objects

- **Matroid (M):** A combinatorial structure generalizing the notion of linear independence.
- **Lattice of Flats (L(M)):** The set of "closed" subsets of the matroid's ground set, ordered by inclusion.
- **Module H(M):** The free `Z[t, t⁻¹]`-module with basis `{F | F ∈ L(M)}`. This is our primary algebraic workspace.
- **Deletion Homomorphism (Δ):** The map from `H(M)` to `H(M\e)` defined in the BV paper.
- **Poincaré Polynomial of the Chow Ring (H_M(t)):** The target object of study from the BHMPW papers. It is a polynomial in `t` satisfying Poincaré duality: `H_M(t) = t^(d-1) * H_M(t⁻¹)`, where `d` is the rank of `M`.
- **Chow-Poincaré Element (C_F):** The central object we will define and study. It's an element in `H(M)` constructed as a sum: `C_F = Σ H_{M^F_G}(t) * G`, where the sum is over all flats `G` of `M^F`, and `M^F_G` is the contraction of `M^F` at `G`.

## 4. Primary Source Documents

The project synthesizes ideas from four main bodies of work, all of which are available in full parsed Markdown form in the `parsed_papers/` directory for easy searching and reference. Additionally, the original LaTeX source files are available in `parsed_papers/texs/` organized by paper:

- **[BV20]: "An algebraic deletion-contraction for Kazhdan-Lusztig polynomials"** by T. Braden and A. Vysogorets.
  - **Contribution:** Provides the core algebraic machinery (`H(M)`, `Δ`, the concept of perversity) that we will adapt.
  - **Source files:** `parsed_papers/texs/bv/KLdeletion.tex`
- **[BHMPW-ssD]: The works on semi-small decomposition and Chow rings of matroids** by T. Braden, J. Huh, J. P. Matherne, N. Proudfoot, and B. Wang.
  - **Contribution:** Defines the object of study (`H_M(t)`), proves its properties using geometric methods, and provides the formula we aim to re-derive algebraically.
  - **Source files:** `parsed_papers/texs/bhmpw/augmentedchow.tex`
- **[ANR24]: "Chow rings of matroids as permutation representations"** by R. Angarone, A. Nathanson, and V. Reiner.
  - **Contribution:** Provides the FY basis and permutation representation perspective for the Chow ring.
  - **Source files:** `parsed_papers/texs/anr/` (multiple .tex files including main.tex, Introduction.tex, Background.tex, etc.)
- **[KL_deletion]: "Notes: Inverse Kazhdan-Lusztig Polynomials under Deletion"**
  - **Contribution:** Provides deletion formulas and the algebraic structure for inverse KL polynomials.
  - **Source files:** Available in parsed Markdown form

## 5. Computational Resources

### SageMath Matroid Functions
The project has access to the complete SageMath matroids module source code, copied from the SageMath repository for local reference. This includes:

- **Complete Source Code:** The `matroids/` folder contains all SageMath matroid implementation files (Cython, Python, and C source files)
- **Comprehensive Function Reference:** `All_Matroid_Functions.md` provides a complete listing of all available matroid functions, organized by category:
  - Main Matroid class methods (100+ functions)
  - Construction functions and catalog matroids
  - Utility functions for printing, labeling, conversions
  - Advanced classes and functions
  - Database and plotting functions
- **Quick Reference:** `sagemath_matroids_reference.md` provides a high-level overview of SageMath's matroid functionality

### Custom Matroid Functions Package
To address limitations in the standard SageMath matroids module, a custom package has been developed:

- **`custom_matroid_functions/`** - Custom implementations that extend or fix SageMath functionality:
  - **`core.py`** - Core utility functions (cmp_elements_key, characteristic_polynomial, whitney_numbers)
  - **`polynomials.py`** - Polynomial computations (Q-polynomials, KL polynomials, inverse KL polynomials)
  - **`chow_polynomials.py`** - Chow polynomial computations with persistent caching
  - **`extensions.py`** - Extended functionality (is_graphic, is_paving)
  - **`__init__.py`** - Package initialization and imports
  - **`README.md`** - Usage documentation and examples

**Key Features:**
- Fixed characteristic polynomial computation (resolves SageMath cmp_elements_key issues)
- Q-polynomial computations for uniform matroids
- Fast inverse Kazhdan-Lusztig polynomial computations
- Chow polynomial computations with persistent JSON caching
- Poincaré polynomial of minors computation
- Reliable graphic matroid detection
- Paving matroid identification

**Usage:** `from custom_matroid_functions import *`

### HM Module (`the-machine/HM_module.py`)
A specialized module implementing the deformed Möbius algebra framework adapted for Chow ring computations:

- **`DeformedMoebiusAlgebra`** - Quantum Möbius algebra with custom bases
- **`ChowBasis`** - Basis adapted for Chow ring computations using Poincaré polynomials of minors
- **`ZetaBasis`** - Classical zeta basis using Kazhdan-Lusztig polynomials
- **Utility functions** - `create_deformed_algebra()`, `create_deformed_algebra_from_lattice()`

**Key Features:**
- Base ring support (ZZ/QQ polynomial rings) with automatic coercion
- Change-of-basis morphisms between all three bases
- Integration with custom matroid functions for Poincaré polynomial computations
- Complete documentation and example usage

**Usage:** 
```python
import sys
sys.path.insert(0, '/path/to/the-machine')
from HM_module import *
```

### Mathematical Definitions
The `definitions/` folder contains comprehensive mathematical definitions for all key objects:
- `mathematical_objects.md` - Complete definitions of matroids, flats, Chow rings, FY basis, etc.
- `computational_framework.md` - Implementation goals and key functions to develop

## 6. Workflow Summary

The project involves:
1.  **Formalization:** Precisely defining all objects and hypotheses in a computational environment (e.g., Python with SymPy/SageMath).
2.  **Experimentation:** Testing the main conjecture on small, concrete examples of matroids (e.g., `U(2,4)`).
3.  **Proof Generation:** Using the insights from the experiments to build a general, formal proof of the main conjecture.
4.  **Derivation:** Showing how the proven conjecture directly implies the deletion-contraction formula for `H_M(t)`.

## 7. Current Development Status

### ✅ Completed Components
- **Custom Matroid Functions Package**: Fully functional with persistent caching
- **HM Module**: Complete deformed Möbius algebra implementation with Chow and Zeta bases
- **Base Ring Issues**: All ZZ vs QQ polynomial ring problems resolved
- **Documentation**: Comprehensive README files and usage examples
- **Module Accessibility**: HM module can be imported and used from other files

### 🔄 In Progress
- **Algebraic Framework Implementation**: Adapting BV framework to Chow ring context
- **Deletion Homomorphism**: Implementing Δ: H(M) → H(M\e) for Chow basis
- **Perversity Conditions**: Defining and testing perversity for Chow-Poincaré elements

### 📋 Next Steps
- **Experimental Testing**: Test conjectures on small matroids using HM module
- **Recursive Formulas**: Develop deletion-contraction formulas for Chow polynomials
- **Proof Development**: Use computational insights to guide theoretical proofs

## 8. Project Organization

- **`definitions/`** - Mathematical definitions and computational framework
- **`parsed_papers/`** - Full parsed Markdown versions of source papers
- **`refs-md-summaries/`** - Detailed summaries of each source paper
- **`matroids/`** - Complete SageMath matroids module source code (ignored by git)
- **`custom_matroid_functions/`** - Custom matroid functions package
- **`the-machine/`** - HM module and experimental code
  - **`HM_module.py`** - Deformed Möbius algebra implementation
  - **`HM_module_README.md`** - Documentation for HM module
  - **`example_usage.sage`** - Example usage of HM module
- **`All_Matroid_Functions.md`** - Complete reference of all SageMath matroid functions
- **`sagemath_matroids_reference.md`** - High-level SageMath matroid functionality overview
- **`TODO_verification_checklist.md`** - Development progress tracking
- **`.gitignore`** - Configured to ignore temporary files and the matroids source folder