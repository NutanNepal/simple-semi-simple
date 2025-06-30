# KL Deletion Paper Summary: Inverse Kazhdan-Lusztig Polynomials under Deletion

## Paper Information
- **Title:** Notes: Inverse Kazhdan-Lusztig Polynomials under Deletion
- **Reference:** KL_deletion.pdf

## Key Definitions and Concepts

### 1. Kazhdan-Lusztig Polynomials
- **PM(t):** The Kazhdan-Lusztig polynomial of a matroid M
- **QM(x):** The inverse Kazhdan-Lusztig polynomial of M
- **Q̂M(x):** Related polynomial defined as Q̂M(x) = (-1)^rk(M) QM(x)

### 2. The Module H(M)
Let H = H(M) be the free ℤ[t, t⁻¹]-module with basis indexed by L(M). Elements of H are formal sums:
```
α = Σ αF · F, αF ∈ ℤ[t, t⁻¹]
```

### 3. The Abelian Subgroup Hp
Hp is an abelian subgroup of H consisting of all α ∈ H such that for every flat F ∈ L(M):
1. αF ∈ ℤ[t]
2. Σ_{G≥F} t^{rk(F)-rk(G)} αG ∈ Pal(0), where Pal(0) is the set of Laurent polynomials f(t) such that f(t) = f(t⁻¹)

### 4. The Elements ζ^F
For any flat F ∈ L(M), an element ζ^F ∈ H is defined as:
```
ζ^F = Σ_{G≤F} t^{rk(F)-rk(G)} P_{M_G^F}(t⁻²) · G
```

### 5. Basis of Hp
**Proposition 2.13:** The set of elements {ζ^F}_{F∈L(M)} forms a ℤ-basis for Hp. Any element β ∈ Hp can be uniquely expressed as:
```
β = Σ_{F∈L(M)} βF(0)ζ^F
```

## Main Results

### 1. BV Deletion Formula (Theorem 2.8 from [1])
For a simple matroid M where e is not a coloop:
```
PM(t) = PM\e(t) - tPMe(t) + Σ_{F∈S} τ(MF∪e) · t^{crk(F)/2} · PM^F(t)
```
where S is the set of all subsets F of E \ e such that both F and F ∪ e are flats of M.

### 2. Main Theorem: Deletion Formula for Q̂M(x)
**Theorem 1:** Let M be a simple matroid and e an element that is not a coloop. Then:
```
Q̂M(x) = Q̂M\e(x) - (1 + x) · Q̂Me(x) - Σ_{G∈S'} τ(Me^G) · x^{rk(G)/2} · Q̂MG(x)
```
where S' = {F ∈ L(M) | e ∈ F and F \ e ∉ L(M)}.

### 3. Module Homomorphism Δ: H(M) → H(M \ e)
The homomorphism Δ is ℤ[t, t⁻¹]-linear and defined on basis elements F ∈ L(M) by:
```
Δ(F) = {
  F                    if F ∌ e
  F \ e                if F ∋ e and F \ e ∉ L(M)
  t⁻¹ · (F \ e)        if F ∋ e and F \ e ∈ L(M)
}
```

### 4. Key Lemmas

**Lemma 2:** Let F ∈ L(M) be a flat such that e ∈ F and F \ e ∉ L(M). Then:
```
Δ(ζ^F) = ζ^{F\e} + Σ_{G∈S(M^F)} τ(MG∪e^F) · ζ^G
```
where S(M^F) = {G ∈ L(M^F) | e ∉ G and G ∪ e ∈ L(M^F)}.

**Lemma 4:** The standard basis {F}_{F∈L(M)} of H(M) satisfies:
```
F = Σ_{G≤F} t^{rk(F)-rk(G)} Q̂_{MG^F}(t⁻²) · ζ^G
```

## Corollaries and Applications

### 1. Corollary 5: Deletion Formula for QM(x)
```
QM(x) = QM\e(x) + (1 + x) · QMe(x) - Σ_{G∈S'} τ(Me^G) · x^{rk(G)/2} · QMG(x)
```

### 2. Corollary 6: Uniform Matroids
For M = Um,d (uniform matroid of rank d on m + d elements with d ≥ 1):
```
QUm,d(x) = QUm-1,d(x) + (1 + x) · QUm,d-1(x) - τ(Um,d-1) · x^{d/2}
```

### 3. Corollary 7: Parallel Connection
For M as the parallel connection of U1,m and U1,n along element e:
```
QM(x) = QU1,m+n-1(x) + (1 + x) · QU1,m-1(x) · QU1,n-1(x)
       - [τ(U1,n-1) · x^{m/2} · QU1,m-1(x) + τ(U1,m-1) · x^{n/2} · QU1,n-1(x) + τ(Me) · x^{(m+n-1)/2}]
```

### 4. Corollary 8: Projective Geometries
For M = PG(r-1, q) (projective geometry of rank r over GF(q)):
```
QM(x) = QM\e(x) + (1 + x) · QPG(r-2,q)(x) - [r-1 choose 1]_q · x · QPG(r-3,q)(x)
```

## Key Insights for Our Project

### 1. Algebraic Framework
- The module H(M) and subgroup Hp provide the foundation for studying KL polynomials
- The ζ^F elements form a natural basis that respects the matroid structure
- The deletion homomorphism Δ provides a concrete algebraic operation

### 2. Deletion-Contraction Structure
- The deletion formulas show how KL polynomials relate under deletion operations
- This provides a model for recursive formulas in our Poincaré polynomial context
- The structure involves both deletion (M \ e) and contraction (Me) operations

### 3. Perverse Elements
- The ζ^F elements are examples of "perverse" elements in the BV framework
- They satisfy specific conditions under the deletion homomorphism
- This provides guidance for defining perverse elements in our H(M) module

### 4. Recursive Formulas
- The deletion formulas provide recursive methods for computing KL polynomials
- These can be adapted for Poincaré polynomial computations
- The formulas involve sums over specific sets of flats

## Computational Implications

### 1. Basis Computations
- The ζ^F basis can be computed systematically from KL polynomials
- The standard basis {F} can be expressed in terms of the ζ^F basis
- This provides computational tools for basis transformations

### 2. Deletion Operations
- The homomorphism Δ can be computed explicitly
- The action of Δ on ζ^F elements follows specific rules
- This enables algorithmic computation of deletion effects

### 3. Recursive Algorithms
- The deletion formulas provide recursive algorithms for KL polynomials
- These can be implemented for specific matroid classes
- The formulas are particularly effective for uniform matroids and projective geometries

### 4. Special Cases
- Uniform matroids have particularly simple deletion formulas
- Projective geometries have known explicit formulas
- These provide test cases for computational implementations

## Connection to Our Research

### 1. Module Structure
- The H(M) module structure provides a model for our algebraic framework
- The ζ^F basis suggests properties for our Chow-Poincaré element C_M
- The deletion homomorphism Δ guides our definition of deletion operations

### 2. Perverse Elements
- The ζ^F elements demonstrate what perverse elements should look like
- Their behavior under Δ provides a template for perversity conditions
- This informs our definition of perverse elements in the Chow ring context

### 3. Recursive Formulas
- The KL deletion formulas provide a model for Poincaré polynomial formulas
- The structure involving sums over flats can be adapted
- The relationship between deletion and contraction operations is crucial

### 4. Computational Framework
- The algebraic methods can be adapted for Poincaré polynomial computations
- The basis transformations provide computational tools
- The recursive structure enables efficient algorithms 