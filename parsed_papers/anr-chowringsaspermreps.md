Proceedings of the 36th Conference on Formal Power
Series and Algebraic Combinatorics (Bochum)

Séminaire Lotharingien de Combinatoire 91B (2024)
Article #24, 12 pp.

Chow rings of matroids as permutation
representations
Robert Angarone* 1 , Anastasia Nathanson†1 , and Victor Reiner‡1
1 University of Minnesota - Twin Cities, Minneapolis MN 55455

Abstract. Given a matroid and a group of its matroid automorphisms, we study the
induced group action on the Chow ring of the matroid. This turns out to always be
a permutation action. Work of Adiprasito, Huh and Katz showed that the Chow ring
satisfies Poincaré duality and the Hard Lefschetz theorem. We lift these to statements
about this permutation action, and suggest further conjectures in this vein.
Keywords: matroid, Chow ring, Koszul, log-concave, unimodal, Kahler package, Burnside ring, equivariant, Polya freqency, real-rooted

1

Introduction

A matroid M is a combinatorial abstraction of lists of vectors v1 , v2 , . . . , vn in a vector
space, recording only the information about which subsets of the vectors are linearly independent or dependent, forgetting their coordinates. In groundbreaking work, Adiprasito, Huh and Katz [1] affirmed long-standing conjectures of Rota–Heron–Welsh and
Mason about vectors and matroids via a new methodology. Their work employed a certain graded Z-algebra A(M) called the Chow ring of M, introduced by Feichtner and
Yuzvinsky [4] as a generalization of the Chow ring of DeConcini and Procesi’s wonderful
compactifications for hyperplane arrangement complements. A remarkable integral Gröbner basis result proven by Feichtner and Yuzvinsky [4, Thm. 2] shows that for a matroid
L
M of rank r + 1 with Chow ring A(M) = rk=0 Ak , each homogeneous component is
free abelian: Ak ∼
= Zak for some Hilbert function ( a0 , a1 , . . . , ar ). A key step in the work
of Adiprasito, Huh and Katz shows not only symmetry and unimodality for the Hilbert
function
ak = ar−k for r ≤ k/2

(1.1)

a 0 ≤ a 1 ≤ · · · ≤ a ⌊ r ⌋ = a ⌈ r ⌉ ≥ · · · ≥ a r −1 ≥ a r ,
2

* angar017@umn.edu
† natha129@umn.edu
‡ reiner@umn.edu

2

(1.2)

Robert Angarone, Anastasia Nathanson, and Victor Reiner

2

but in fact proves that A(M) enjoys a trio of properties referred to as the Kähler package,
reviewed in Section 2.2 below. The first of these properties is Poincaré duality, proving
(1.1) via a natural Z-module isomorphism Ar−k ∼
= HomZ ( Ak , Z). The second property,
called the Hard Lefschetz Theorem, shows that after tensoring over Z with R to obtain
L
k , one can find Lefschetz elements ω in A1 such that multiplication by
A(M)R = k=0 AR
R
k → Ar −k for k ≤ r . In particular, multiplication by
ω r−2k give R-linear isomorphisms AR
R
2
k → Ak+1 is injective for k < r , strengthening the unimodality (1.2).
ω mapping AR
R
2
We are interested in how these Poincaré duality and Hard Lefschetz properties interact
with the group G := Aut(M) of symmetries of the matroid M. It is not hard to check
that G acts via graded Z-algebra automorphisms on A(M), giving ZG-module struck . One can also check (see the
tures on each Ak , and RG-module structures on each AR
proof of Corollary 6 below) that Ar ∼
= Z with trivial G-action. From this, the Poincaré
duality pairing immediately gives rise to a ZG-module isomorphism
Ar −k ∼
= HomZ ( Ak , Z)

(1.3)

where g in G acts on φ in HomZ ( Ak , Z) via φ 7→ φ ◦ g−1 ; similarly Ar−k ∼
= HomR ( Ak , R)
as RG-modules. Furthermore, it is not hard to check (see Corollary 6 below) that one
can pick an explicit Lefschetz element ω as in [1] which is G-fixed, giving RG-module
isomorphisms and injections
∼

k
r −k
AR
−→ AR

for r ≤

a 7−→ a · ω r−2k

k
2

k +1
k
,→ AR
AR

a 7−→ a · ω.

for r <

k
2
(1.4)

Our goal is to use Feichtner and Yuzvinsky’s Gröbner basis result to prove a combinatorial strengthening of the isomorphisms and injections (1.3), (1.4). To this end, recall
that the matroid M can be specified by its family F of flats; then the Chow ring A(M)
is presented as a quotient of the polynomial ring S := Z[ x F ] having one variable x F for
each nonempty flat F in F \ {∅}. The presentation takes the form A(M) := S/( I + J )
where I, J are certain ideals of S defined more precisely in Definition 1 below.
Feichtner and Yuzvinsky exhibited a Gröbner basis for I + J that leads to the following standard monomial Z-basis for A(M), which we call the FY-monomials of M:
m

1 m2
ℓ
FY := { x m
F1 x F2 · · · x F : (∅ = : F0 ) ⊊ F1 ⊊ F2 ⊊ · · · ⊊ Fℓ , and mi ≤ rk( Fi ) − rk( Fi −1 ) − 1}.

ℓ

Here rk( F ) denotes the matroid rank of the flat F. The subset FYk of FY-monomials
mℓ
k
1
xm
F1 · · · x F of total degree m1 + · · · + mℓ = k then gives a Z-basis for A . One can readily
ℓ

check (see Corollary 4 below) that the group G = Aut(M) permutes the Z-basis FYk for
Ak , endowing Ak with the structure of a permutation representation, or G-set. Our main
result is this strengthening of the isomorphisms and injections seen in (1.3), (1.4).

Chow rings of matroids as permutation representations

3

Theorem 1. For every matroid M of rank r + 1, there exist
∼

(i) G-equivariant bijections π : FYk −→ FYr−k for k ≤ 2r , and
(ii) G-equivariant injections λ : FYk ,→ FYk+1 for k < 2r .

2

Background

Among the many definitions of a matroid M on ground set E, the most useful here
specifies its collection of flats F ⊊ 2E , satisfying certain axioms. When ordered by inclusion the collection of flats (F, ⊆) forms a geometric lattice; in an abuse of notation,
we will use F to refer to both the lattice and the set. This lattice is ranked, with rank
function denoted rk( F ). The rank of the matroid M itself is defined to be rk( E), and
we assume throughout that rk( E) = r + 1. An automorphism of the matroid M is any
permutation g : E → E of the ground set E that carries flats to flats: for all F in F one has
g( F ) in F. Let G = Aut(M) denote the group of all automorphisms of M. Since such
automorphisms respect the partial order via inclusion on F, they also preserve the rank
function: rk( g( F )) = rk( F ) for all g in G and F in F.

2.1

Chow Rings

As defined in the Introduction, Feichtner and Yuzvinsky [4] introduced the Chow ring
A(M) of a matroid M.
Definition 1. The Chow ring A(M) of a matroid M is the quotient Z-algebra
A(M) := S/( I + J )
where S = Z[ x F ] is a polynomial ring having one variable x F for each nonempty flat
F ∈ F \ {∅}, and where I, J are the following ideals of S:
• I is generated by products x F x F′ where F, F ′ are incomparable flats,
• J is generated by the linear elements

∑ xF for each atom a in the lattice F.

a∈ F ∈F

The presentation of the Chow ring A(M) only uses the information about the partial
order on the lattice of flats F has some consequences. For one, the Chow ring depends
only upon the associated simple matroid of M (one without loops and parallel edges);
hence, we assume all matroids to be such. Another consequence is that any element g in
G = Aut(M) will send the generators of the ideals I, J to other such generators. Thus
I + J is a G-stable ideal, and G acts on A(M).

Robert Angarone, Anastasia Nathanson, and Victor Reiner

4

Note if one considers S = Z[ x F ] as a graded Z-algebra, then the ideals I, J are generated by homogeneous elements. Hence the quotient A(M) = S/( I + J ) inherits the
L
k
structure of a graded Z-algebra A(M) = ∞
k=0 A . Since the action of G = Aut(M)
on the Chow ring preserves rank and hence degree, both A(M) and each homogeneous
component Ak become ZG-modules.
The following crucial result appears as [4, Thm. 2]. To state it, define an FY-monomial
order on S = Z[ x F ]∅̸= F∈F to be any monomial order based on a linear order of the
variables with x F > x F′ if F ⊊ F ′ .
Theorem 2. Given a matroid M and any FY-monomial order on S = Z[ x F ]∅̸= F∈F , the ideal
I + J presenting A(M) = S/( I + J ) has a monic Gröbner basis { g F,F′ } indexed by F ̸= F ′ in
F, with g F,F′ and their initial terms in≺ ( g F,F′ ) as shown here:
condition on F ̸= F ′ in F

g F,F′

in≺ ( g F,F′ )

F, F ′ non-nested

x F x F′

x F x F′

rk( F′ )−rk( F)





′′ 
xF 
x
∑
F
 ′′


∅ ̸= F ⊊ F′

rk( F ′ )−rk( F )

x F · x F′

F ∈F:
F ′′ ⊇ F ′

rk( F′ )



rk( F ′ )



 ∑ x F′′ 
 ′′


∅ = F ⊊ F′

x F′

F ∈F:
F ′′ ⊇ F ′

Corollary 3. ([4, Cor. 1]) For a matroid M of rank r + 1, the Chow ring A(M) has these
properties:
(i) A(M) is free as a Z-module, with Z-basis given by the set of what we call FY-monomials
m

1 m2
ℓ
FY := { x m
F1 x F2 · · · x F : F1 ⊊ · · · ⊊ Fℓ ∈ F, and mi ≤ rk( Fi ) − rk( Fi −1 ) − 1}. (2.1)

ℓ

(ii) A(M) vanishes in degrees strictly above r, that is, A(M) =

Lr

k
k =0 A .

(iii) Ar has Z-basis { xrE }, and so a Z-module isomorphism deg : Ar −→ Z sending xrE 7−→ 1.

Chow rings of matroids as permutation representations

5

Assertions (ii) and (iii) follow immediately from the first. To see this, note that the
mℓ
1 m2
typical FY-monomial x m
F1 x F2 · · · x F , has total degree
ℓ

ℓ

ℓ

i =1

i =1

∑ mi ≤ ∑ (rk( Fi ) − rk( Fi−1 ) − 1) = rk( Fℓ ) − ℓ ≤ (r + 1) − 1 = r + 1.

Equality here occurs only if ℓ = 1 and Fℓ = E, in which case the FY-monomial is xrE .
For any matroid automorphism g, the fact that rk( g( F )) = rk( F ) for every flat F in F
implies that g sends any FY-monomial to another FY-monomial:
g

m

m

1 m2
1
ℓ
xm
7−→ x m
x m2 · · · x g(ℓF ) .
F1 x F2 · · · x F
g( F ) g( F )

ℓ

2

1

ℓ

This has a corollary, inspired by work of H.-C. Liao on Boolean matroids [8, Thm. 2.5].
Corollary 4. For any matroid M, the group G = Aut(M) permutes the set FY, as well as
its subset of degree k monomials FYk ⊂ FY. Consequently, the ZG-modules on the Chow ring
A(M) and each of its homogeneous components Ak lift to G-permutation representations on FY
and each FYk .
Example 1. Let M = U4,5 be the uniform matroid of rank 4 on E = {1, 2, 3, 4, 5}, associated to a list of 5 generic vectors v1 , v2 , v3 , v4 , v5 in a 4-dimensional vector space, so that
any quadruple vi , v j , vk , vℓ is linearly independent. One has these flats of various ranks:
rank

flats F ∈ F

0
1
2
3
4

∅
1, 2, 3, 4, 5
12, 13, 14, 15, 23, 24, 25, 34, 35, 45
123, 124, 125, 134, 135, 145, 234, 235, 245, 345
E = 12345

The Chow ring A(M) = S/( I + J ), where S = Z[ xi , x jk , xℓmn , x E ] with {i }, { j, k}, {ℓ, m, n}
running through all one, two and three-element subsets of E = {1, 2, 3, 4, 5}, and
!


.
I = x F x F′
,
J = xi + ∑ x jk +
∑ xℓmn + xE
F ̸⊂ F ′ ,F ′ ̸⊂ F

1≤ℓ<m<n≤5
i ∈{ℓ,m,n}

1≤ j < k ≤5
i ∈{ j,k}

i =1,2,3,4,5

The FY-monomial bases for A0 , A1 , A2 , A3 are shown here, together with the G-equivariant
maps λ:
FY0
FY1
FY2
FY3
1

λ

7−→

xE

7−→

λ

x2E

xijk

7−→

λ

2
xijk

xij

7−→ xij · x E

λ

x3E

Robert Angarone, Anastasia Nathanson, and Victor Reiner

6

Thus in this case, the ranks of the free Z-modules ( A0 , A1 , A2 , A3 ) form the symmetric, unimodal sequence ( a0 , a1 , a2 , a3 ) = (1, 21, 21, 1). Here the bijection π : FY0 → FY3
necessarily maps 1 7−→ x3E , and the bijection π : FY1 → FY2 coincides with the map
λ : FY1 → FY2 above.

2.2

The Kähler package

The following theorem on the Kähler package for A(M) compiles some of the main
results of the work of Adiprasito, Huh and Katz [1].
Theorem 5. For a matroid M of rank r + 1, the Chow ring A(M) satisfies the Kähler package:
• (Poincaré duality) For every k ≤ 2r , one has a perfect Z-bilinear pairing
Ak × Ar−k −→ Z

( a, b) 7−→ deg( a · b)
k
• (Hard Lefschetz) Tensoring over Z with R, the (real) Chow ring AR (M) = ∑rk=0 AR
1
r
−
2k
contains Lefschetz elements ω in AR , meaning that a 7→ a · ω
is an R-linear isor −k
r
k
morphism AR → AR for k ≤ 2 . In particular, multiplication by ω is an injection
k → Ak+1 for k < r .
AR
R
2

• (Hodge-Riemann-Minkowski inequalities) The Lefschetz elements ω define quadratic forms
k that become positive definite upon restriction to the
a 7−→ (−1)k deg( a · ω r−2k · a) on AR
k −→ Ar −k+1 that sends a 7 −→ a · ω r −2k+1 .
kernel of the map AR
R
In fact, they show that one obtains a Lefschetz element ω whenever ω = ∑∅̸= F∈F c F x F
has coefficients c F coming from restricting to F any function A 7→ c A that maps 2E → R
and satisfies these two properties:
(1) the strict submodular inequality c A + c B > c A∩ B + c A∪ B for all A ̸= B, and
(2) c∅ = c E = 0.
This has consequences for G acting on A(M) and each Ak . Properties (1) and (2)
above are refined by Theorem 1’s parts (i) and (ii) respectively.
Corollary 6. For any matroid M, one has an isomorphism of ZG-modules Ar−k → Ak for each
k → Ak+1 which are injective for k < r .
k ≤ 2r and RG-module maps AR
R
2

Chow rings of matroids as permutation representations

3

7

Results

We recall the statement of the theorem, involving the FY-monomial Z-basis for A(M)
in Corollary 3:
m

1 m2
ℓ
FY := { x m
F1 x F2 · · · x F : ⊊ F1 ⊊ F2 ⊊ · · · ⊊ Fℓ in F, and mi ≤ rk( Fi ) − rk( Fi −1 ) − 1}

ℓ

This also means that the FY-monomials FYk of degree k form a Z-basis for Ak for each
k = 0, 1, 2, . . . , r.
Theorem 1 For every matroid M of rank r + 1, there exist
∼

(i) G-equivariant bijections π : FYk −→ FYr−k for k ≤ 2r , and
(ii) G-equivariant injections λ : FYk ,→ FYk+1 for k < 2r .
The prove this, we organize monomials according to the fibers of the following map.
m

1
ℓ
Definition 2. Define the extended support supp+ ( a) ⊂ F of an FY-monomial a = x m
F1 · · · x Fℓ

by
{ F , . . . , F } ∪ { E} if F ⊊ E,
1
ℓ
ℓ
supp+ ( a) := { F1 , . . . , Fℓ } ∪ { E} =
{ F1 , . . . , Fℓ }
if Fℓ = E.

Define a partial order <+ on the FY-monomials in which a <+ b if a divides b and
supp+ ( a) = supp+ (b).
For integers p < q, let [ p, q] denote the integer linear order inclusively from p to q.
Given a sequence of such pairs pi < qi for i = 1, 2, . . . , m, let
n

∏ [ p i , q i ] = [ p1 , q1 ] × [ p2 , q2 ] × · · · × [ p m , q m ]

(3.1)

i =1

denote their Cartesian product, partially ordered componentwise.
Proposition 7. For any nested flag { F1 ⊊ · · · ⊊ Fℓ ⊊ E} in F containing E, with con1
ventions F0 := ∅ and Fℓ+1 := E, the fiber supp−
+ { F1 , . . . , Fℓ , E } is the set of monomials
mℓ mℓ+1
1 m2
{ xm
} satisfying these inequalities:
F1 x F2 · · · x F x E
ℓ

1 ≤ mi ≤ rk( Fi ) − rk( Fi−1 ) − 1 for i ≤ ℓ,
0 ≤ mℓ+1 ≤ rk( E) − rk( Fℓ ) − 1 = r − rk( Fℓ ).
1
Consequently, the minimum and maximum degree of monomials in supp−
+ { F1 , . . . , Fℓ , E } are ℓ
and r − ℓ, and one has a poset isomorphism
1
(supp−
+ { F1 , . . . , Fℓ , E }, <+ ) −→

ℓ

∏[1, rk( Fi ) − rk( Fi−1 ) − 1] × [0, r − rk( Fℓ )]
i =1

m

m

ℓ+1
1 m2
ℓ
xm
7−→ (m1 , m2 , . . . , mℓ , mℓ+1 ).
F1 x F2 · · · x F x E
ℓ

Robert Angarone, Anastasia Nathanson, and Victor Reiner

8

Most assertions of the proposition are immediate from the definition of the order on FYmonomials <+ and the map supp+ . The minimum and maximum degrees of monomials
1
in supp−
+ { F1 , . . . , Fℓ , E }) are achieved by
ℓ

deg

∏ xFi

deg( x1F1 x1F2 · · · x1Fℓ x0E ) = ℓ
!

rk( Fi )−rk( Fi )−1

rk( E)−rk( Fℓ )−1)

· xE

i =1

and

ℓ+1

= ∑ rk( Fi ) − rk( Fi−1 ) − 1



i =1

= rk( E) − (ℓ + 1)
= r − ℓ.
The idea behind the proof of Theorem 1 stems from the observation that all products
of chains, as in (3.1), have symmetric chain decompositions, which can then be pulled back
1
to each fiber supp−
+ { F1 , . . . , Fℓ , E }.
Definition 3. A symmetric chain decomposition (SCD) of a finite ranked poset P of rank
F
r is a disjoint decomposition P = it=1 Ci in which each Ci is a totally ordered subset
containing one element of each rank {ρi , ρi + 1, . . . , r − ρi − 1, r − ρi } for some ρi ≤ ⌊ 2r ⌋.
It is not hard to check that when posets P1 , P2 each have an SCD, then so does their
Cartesian product. In particular, all products of chains have an SCD. Fix one such SCD for
each product poset in (3.1), once and for all, and use the isomorphisms from Proposition 7
1
to induce an SCD on each fiber supp−
+ { F1 , . . . , Fℓ , E }.
Example 2. Assume M has rk( E) = 10 = r + 1 with r = 9, and one has a pair of nested
1
′
flats F ⊂ F ′ with rk( F ) = 3, rk( F ′ ) = 7. Then the poset supp−
+ { F, F , E } and one choice
of SCD for it look as follows:
x2F x3F′ x2E

x2F x3F′ x2E

x2F x3F′ x E x F x3F′ x2E x2F x2F′ x2E

x2F x3F′ x E x F x3F′ x2E x2F x2F′ x2E

x2F x3F′ x F x3F′ x E x2F x2F′ x E x F x2F′ x2E x2F x F′ x2E

x2F x3F′ x F x3F′ x E x2F x2F′ x E x F x2F′ x2E x2F x F′ x2E

x F x3F′

x F x3F′

x2F x2F′ x F x2F′ x E x2F x F′ x E x F x F′ x2E
x F x2F′

x2F x F′ x F x F′ x E
x F x F′

x2F x2F′ x F x2F′ x E x2F x F′ x E x F x F′ x2E
x F x2F′

x2F x F′ x F x F′ x E
x F x F′

Chow rings of matroids as permutation representations

4

9

Further questions and conjectures

So far, we have mentioned that the unimodality statement (1.2), asserting for k < 2r that
one has ak ≤ ak+1 , is weaker than the statement in Corollary 6 asserting that there are
k → Ak+1 , which is weaker than Theorem 1(ii) asserting
injective RG-module maps AR
R
that there are injective G-equivariant maps of the G-sets FYk ,→ FYk+1 . Here, we wish to
consider not only unimodality for ( a0 , a1 , . . . , ar ), but other properties like log-concavity,
the Pólya frequency property, and how to similarly lift them to statements regarding RGmodules and G-permutation representations. In phrasing this, it helps to consider the
character and Burnside rings.
Definition 4. For a finite group G, its virtual (complex) character ring RC ( G ) is the free Zsubmodule of the ring of (conjugacy) class functions { f : G → C}, having as a Z-basis
the irreducible complex characters of G. If a character χ can be written as a positive
linear combination of irreducible characters of G, we say that χ is a genuine character,
and write χ ≥ RC (G) 0.
Similarly, one can define its Burnside ring B( G ) by now having as basis the isomorphism classes [ X ] of finite G-sets X. Then B( G ) is the Z-module that mods out by the
span of all elements [ X ⊔ Y ] − ([ X ] + [Y ]) and if b ∈ B( G ) can be written as a positive
linear combination of isomorphism classes, then b is a genuine permutation representation,
and b ≥ B(G) 0.

4.1

PF sequences and log-concavity

For a sequence of positive real numbers ( a0 , a1 , . . . , ar ), the property of unimodality lies at
the bottom of a hierarchy of concepts
unimodal ⇐

PF2
⇐
∥
(strongly) log-concave

PF3

⇐ ··· ⇐

PF∞
∥
PF

(4.1)

which we next review, along with their equivariant and Burnside ring extensions.
Definition 5. Say a sequence of positive reals ( a0 , a1 , . . . , ar ) is strongly log-concave (or
PF2 ) if 0 ≤ i ≤ j ≤ k ≤ ℓ ≤ r and i + ℓ = j + k implies
"
#
a j aℓ
ai aℓ ≤ a j ak , or equivalently, det
≥ 0.
ai a k

10

Robert Angarone, Anastasia Nathanson, and Victor Reiner

For ℓ = 2, 3, 4, . . ., say that the sequence is PFℓ if the associated (infinite) Toeplitz matrix


a 0 a 1 a 2 · · · a r −1 a r
0
0 ···


 0 a 0 a 1 · · · a r −2 a r −1 a r
0 · · ·

T ( a0 , . . . , ar ) : = 
 0 0 a 0 · · · a r −3 a r −2 a r −1 a r · · · 
. . .
..
..
..
..
.. . . 
.. .. ..
.
.
.
.
.
.
has all nonnegative square minor subdeterminants of size m × m for 1 ≤ m ≤ ℓ. Say that
the sequence is a Pólya frequency sequence (or PF∞ , or just PF) if it is PFℓ for all ℓ = 2, 3, . . ..
Definition 6. For a finite group G and (genuine, nonzero) CG-modules ( A0 , A1 , . . . , Ar ),
define the analogous notions of equivariant unimodality, equivariant strong log-concavity,
equivariant PFr or PF∞ by replacing the numerical inequalities in Definition 5 by inequalities in RC ( G ), or, similarly, one can define all these concepts to be Burnside if these
inequalities are in the Burnside ring B( G ).
We’ve seen for Chow rings A(M) of rank r + 1 matroids M, and G = Aut(M),
the sequence ( a0 , a1 , . . . , ar ) with ak := rkZ Ak is unimodal; after tensoring with C, the
r ) is equivariantly unimodal; and the sequence of
sequence of CG-modules ( A0C , A1C , . . . , AC
G-sets (FY0 , FY1 , . . . , FYr ) is Burnside unimodal.
Conjecture 1. In the Chow ring of a rank r + 1 matroid M, one has that
(i) (Ferroni-Schröter [6, Conj. 10.19]) ( a0 , . . . , ar ) is PF∞ .
r ) is equivariantly PF .
(ii) ( A0C , . . . , AC
∞

(iii) (FY0 , . . . , FYr ) is Burnside PF2 (Burnside log-concave).
Of course, in Conjecture 1, assertion (ii) implies assertion (i). However the same is
not true of assertion (iii): it would only imply the weaker PF2 part of the conjectural
assertion (ii), and only imply the PF2 part of Ferroni and Schröter’s assertion (i), but not
their PF∞ assertions. We have some evidence for the following two further conjectures.
Conjecture 2. For a Boolean matroid M of rank n and i ≤ j ≤ k ≤ ℓ with i + ℓ = j + k,
not only is the element [FY j ][FYk ] − [FYi ][FYℓ ] ≥ B(Sn ) 0, so that it is a genuine permutation
representation, but furthermore one whose orbit-stabilizers are all Young subgroups Sλ .

Chow rings of matroids as permutation representations

11

Conjecture 3. For a matroid M of rank r + 1 with Chow ring A(M), and any composition
α = (α1 , . . . , αℓ ) with m := ∑i α ≤ r, the analogous Toeplitz minors of G-sets have


[FYα1 ] [FYα1 +α2 ] [FYα1 +α2 +α3 ] · · ·
[FYm ]


 [FY0 ]
[FYα2 ]
[FYα2 +α3 ]
···
[FYm−α1 ] 

0
α3
m−(α1 +α2 ) 
 0
[
FY
]
[
FY
]
·
·
·
[
FY
]


det 
..
 ≥ B(G) 0.
 0

0
.
 .

.
 .
αℓ−1 +αℓ 
.
.
.
[
FY
]


0
0
···
[FY0 ]
[FYαℓ ]

4.2

Further Questions

So far, we have focused on the Chow ring of a matroid M using its maximal building set.
One relevant example of such a building set is the minimal building set, which is
stable under the full automorphism group Aut(M), and which arises, for example, in
the study of the moduli space M0,n of genus 0 curves with n marked points; see, e.g.,
Dotsenko [3], Gibney and Maclagan [7].
Question 4. Does the analogue of Theorem 1 hold for the Chow ring of a matroid M with respect
to any G-stable building set? In particular, what about the minimal building set?
In [9, Lem. 3.1], Stembridge provides a generating function for the symmetric group
representations on each graded component of the Chow ring for all Boolean matroids;
see also Liao [8]. Furthermore, Stembridge’s expression exhibits them as permutation
representations, whose orbit-stabilizers are all Young subgroups in the symmetric group.
Question 5. Can one provide such explicit expressions as permutation representations for other
families of matroids with symmetry?
Hilbert functions ( a0 , a1 , . . . , ar ) for Chow rings of rank r + 1 matroids are not only
symmetric and unimodal, but satisfy the stronger condition of γ-positivity, as shown by
: one has nonnegativity for all coefficients γ = (γ0 , γ1 , . . . , γ⌊ r ⌋ ) appearing in the unique
2
expansion
r

⌊ 2r ⌋

∑ ai t = ∑ γi ti (1 + t)r−2i .

i =0

i

i =0

This has been shown, independently by Ferroni, Matherne, Stevens and Vecchi [5, Thm.
3.25] and by Wang (see [5, p. 29]), that the γ-positivity for Hilbert series of Chow rings
of matroids follows from results of [2].
One also has the notion of equivariant γ-positivity for a sequence of G-representations
( A0 , A1 , . . . , Ar ): upon replacing each ai with the element [ Ai ] of RC ( G ), one asks that
the uniquely defined coefficients γi in RC ( G ) have γi ≥ RC (G) 0.

Robert Angarone, Anastasia Nathanson, and Victor Reiner

12

Conjecture 6. For any matroid M of rank r + 1 and its Chow ring A(M) =
r ) is equivariantly γ-positive.
sequence of G-representations ( A0C , A1C , . . . , AC

L

i
i A , the

Acknowledgements
The authors thank Alessio D’Ali, Chris Eur, Luis Ferroni, Matt Larson, Hsin-Chieh Liao,
Diane Maclagan, Matt Maestroni, Jacob Matherne, Connor Simpson, Lorenzo Vecchi
and Peter Webb for helpful conversations and references. They thank Trevor Karn for
his wonderful Sage/Cocalc code that checks whether a symmetric group representation is a permutation representation. The authors received partial support from NSF
grants DMS-1949896, DMS-1745638, DMS-2053288. Second author received partial support from PROM project no. POWR.03.03.00-00-PN13/18.

References
[1]

K. Adiprasito, J. Huh, and E. Katz. “Hodge theory for combinatorial geometries”. Ann. of
Math. (2) 188.2 (2018), pp. 381–452. doi.

[2]

T. Braden, J. Huh, J. P. Matherne, N. Proudfoot, and B. Wang. “A semi-small decomposition
of the Chow ring of a matroid”. Adv. Math. 409 (2022), Paper No. 108646, 49. doi.

[3]

V. Dotsenko. “Homotopy invariants for M0,n via Koszul duality”. Invent. Math. 228.1 (2022),
pp. 77–106. doi.

[4]

E. M. Feichtner and S. Yuzvinsky. “Chow rings of toric varieties defined by atomic lattices”.
Invent. Math. 155.3 (2004), pp. 515–536. doi.

[5]

L. Ferroni, J. P. Matherne, M. Stevens, and L. Vecchi. “Hilbert-Poincaré series of matroid
Chow rings and intersection cohomology”. 2023. arXiv:2212.03190.

[6]

L. Ferroni and B. Schröter. “Valuative invariants for large classes of matroids”. 2022. arXiv:
2208.04893.

[7]

A. Gibney and D. Maclagan. “Equations for Chow and Hilbert quotients”. Algebra Number
Theory 4.7 (2010), pp. 855–885. doi.

[8]

H.-C. Liao. “Stembridge codes and Chow rings”. 2022. arXiv:2212.05362.

[9]

J. R. Stembridge. “Eulerian numbers, tableaux, and the Betti numbers of a toric variety”.
Discrete Math. 99.1-3 (1992), pp. 307–320. doi.

