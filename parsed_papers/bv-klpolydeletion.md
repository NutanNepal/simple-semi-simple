Kazhdan–Lusztig polynomials of matroids
under deletion
Tom Braden

Artem Vysogorets

Department of Mathematics and Statistics
University of Massachusetts Amherst
Amherst, MA, U.S.A.

Center for Data Science
New York University
New York, NY, U.S.A.

braden@math.umass.edu

artem@vysogorets.org

Submitted: Sept 22, 2019; Accepted: Jan 6, 2020; Published: Jan 24, 2020
c The authors. Released under the CC BY-ND license (International 4.0).

Abstract
We present a formula which relates the Kazhdan–Lusztig polynomial of a matroid M , as defined by Elias, Proudfoot and Wakefield, to the Kazhdan–Lusztig
polynomials of the matroid obtained by deleting an element, and various contractions and localizations of M . We give a number of applications of our formula to
Kazhdan–Lusztig polynomials of graphic matroids, including a simple formula for
the Kazhdan–Lusztig polynomial of a parallel connection graph.
Mathematics Subject Classifications: 05B35

1

Introduction

In [EPW16], Elias, Proudfoot and Wakefield defined a polynomial invariant PM (t) associated to any matroid M , which they called the Kazhdan–Lusztig polynomial of
M . Their definition is formally similar to the polynomials Px,y (t) that were defined by
Kazhdan and Lusztig [KL79] for elements x, y in a Coxeter group W . The coefficients
of PM (t) depend only on the lattice of flats L(M ), and in fact they are integral linear
combinations of the flag Whitney numbers counting chains of flats with specified ranks.
In this paper, we study how PM (t) behaves under deletion of an element from the
ground set. Our main result, Theorem 2.8, is a formula relating the Kazhdan–Lusztig
polynomial of the deletion M r e to the Kazhdan–Lusztig polynomials of M and various
contractions and localizations of M . Assume that M is a simple matroid, and that e is
not a coloop of M . Then our formula says that
X
PM (t) = PM re (t) − tPMe (t) +
τ (MF ∪e ) t(crk F )/2 PM F (t).
(1)
F ∈S

the electronic journal of combinatorics 27(1) (2020), #P1.17

1

Here the sum is taken over the set S of all subsets F of E r e such that F and F ∪ e
are both flats of M (any such F is automatically also a flat of M r e), and τ (M ) is the
coefficient of t(rk M −1)/2 in PM (t) if rk M is odd, and zero otherwise. We also give a similar
formula for the closely related Z-polynomial
X
ZM (t) =
trk F PMF (t),
F ∈L(M )

which was introduced in [PXY18].
Since all of the matroids appearing on the right side of (1) have a smaller ground set
than M does, it is natural to apply this formula to inductive computations of PM (t). The
challenge to carrying this out successfully is the complexity of the sum in the last term.
In the final part of the paper we present some applications of our formula to graphic
matroids where the sum simplifies enough to make the formula useful.
In particular, we get a very simple formula for Kazhdan–Lusztig polynomials of parallel connection graphs: if G is obtained by gluing graphs H1 and H2 at an edge e
common to both, and H1 r e, H2 r e are both connected, then
PG (t) = PGre (t) − tPH1 (t)PH2 (t).
Here we put PG (t) = PMG (t) when G is a graph. We use this result to give a simpler
proof of a formula of Liu, Xie and Yang [LXY] for the Kazhdan–Lusztig polynomials of
fan graphs.
1.1

Motivation from algebraic geometry

Our results and our methods in this paper are purely combinatorial, but the motivation
comes from algebraic geometry. In this section, which is not needed for the rest of the
paper, we briefly explain the geometry behind the formula (1).
The Kazhdan–Lusztig polynomial of a realizable matroid M is the local intersection
cohomology Poincaré polynomial of a variety defined as follows. Suppose that M is
realized by a spanning collection w1 , . . . , wn of nonzero vectors in a vector space W ∼
= Cd ,
where d = rk M . This induces a surjective map Cn → W , and dualizing gives an injection
W ∗ → Cn . Let V ∼
= Cd be the image of this map, and define Y = Y (w1 , . . . , wn ) to
be the closure of V inside (P1C )n . Then PM (t) is the Poincaré polynomial of the local
intersection cohomology of Y at the most singular point ∞n and ZM (t) is the Poincaré
polynomial of the total intersection cohomology IH • (Y ; Q). (All intersection cohomology
groups considered in this discussion vanish in odd degrees, and all Poincaré polynomials
should be taken in t1/2 .)
The variety Y was called the Schubert variety of V in [PXY18], because of the
similarities it has with the geometry of Schubert
`varieties in flag varieties of reductive
groups. In particular, Y has a stratification Y = F ∈L(M ) CF by affine spaces CF ∼
= Crk F
indexed by flats of M ; the strata are orbits of the natural action of the additive group
(V, +) on Y . Closures of strata and normal slices to strata are again varieties of the same
type. (Note that for a Schubert variety in a flag variety, a normal slice to a Schubert cell
the electronic journal of combinatorics 27(1) (2020), #P1.17

2

cannot in general be identified with another Schubert variety.) The closure Y F := CF of
a stratum is isomorphic to the variety Y (wi1 , . . . , wik ), where F = {i1 , . . . , ik }, and the
vector space W is replaced by the span of wi1 , . . . , wik . A normal slice to Y at a point
of CF is isomorphic to Y (w̄j1 , . . . , w̄jr ), where {j1 , . . . , jr } = {1, . . . , n} r F and w̄j is
the image of wj in the quotient W/ span(wi1 , . . . , wik ). These varieties correspond to the
localization and contraction matroids M F and MF , respectively. (See the beginning of
the next section for definitions and notation of localization and contraction.)
Suppose that the element we are deleting from M is e = n. Then our assumption
that n is not a coloop means that w1 , . . . , wn−1 still span W , and following the same
construction shows that the variety Y 0 = Y (w1 , . . . , wn−1 ) associated to the deletion M re
is the image of Y under the projection (P1 )n → (P1 )n−1 which forgets the last factor. Let
p: Y →
Y 0 denote the map induced by this projection. We can define a stratification
`
Y 0 = G∈L(M re) CG0 the same way as before, and the map p : Y → Y 0 sends strata to
strata.
The fibers of p are easy to describe: either p−1 (x) is a single point or it is isomorphic
to P1 , and it is P1 if and only if x lies in a stratum CF0 where F and F ∪ e are flats of
M , i.e. F is in the set S summed over in (1). Because of this, the decomposition theorem
of Beilinson, Bernstein, Deligne and Gabber takes a particularly simple form: the direct
image p∗ IC(Y ; Q) of the intersection complex of X is isomorphic to a direct sum
M
(2)
IC(Y 0 ; Q) ⊕
IC(CF0 ; Q)⊕τ (MF ∪e ) [−(crk F )/2].
F ∈S

Our formula (1) comes from taking the stalk cohomology of p∗ IC(Y ; Q) at the point
stratum C∅0 . By proper base change this is
H• (IC(Y ; Q)|p−1 (C∅0 ) ) = H• (IC(Y ; Q)|C∅ ∪Ce ),
which has Poincaré polynomial PM (t)+tPMe (t), while the stalk of the sum (2) has Poincaré
polynomial given by the remaining terms of (1).
Our formula is analogous to the convolution formula
X
µ(z, w)Cz
(3)
Cs Cw = Csw +
sz<z

that governs Kazhdan–Lusztig basis elements {Cx }x∈W in the Hecke algebra H(W) (see
[Hum90, equation (22)], for instance). Here s is a simple reflection and sw > w. This
e → Xsw which is similar to our map Y → Y 0 .
formula arises from analyzing a map X
e is a P1 -bundle over a smaller Schubert variety Xw .
Here Xsw is a Schubert variety, and X
Again the fibers are either points or P1 , and the analysis of the decomposition theorem is
essentially the same.
There is one important difference, however. In (3) all of the terms except Csw involve
basis elements Cz for z ⩽ w, so it gives a recursive computation of Csw . In fact this formula
was used by Kazhdan and Lusztig [KL79] to prove the existence of the basis elements Cx .
e is Cs Cw , reflecting the structure of X
e as a P1 -bundle.
The expression corresponding to X
the electronic journal of combinatorics 27(1) (2020), #P1.17

3

On the other hand, in our situation the variety Y “upstairs” is in general more complicated
than Y 0 , and doesn’t have a simple relation with lower-dimensional varieties of the same
type. As a result, the power of our formula in inductive computations and proofs is more
limited.

2

The deletion formula

2.1

Matroid terminology

Let M be a matroid on a ground set E. One of the many equivalent ways to define a
matroid is by its flats, which are subsets of E satisfying
• E is a flat,
• if F, G are flats, then F ∩ G is a flat, and
• for any flat F , the complement E r F is partitioned by the sets G r F where G
runs over all flats which cover F .
The set of all flats ordered by inclusion is a ranked lattice which we denote L(M ), and we
let rk : L(M ) → Z⩾0 be its rank function. All of the invariants we consider depend only
on L(M ) up to isomorphism as a ranked poset.
We will assume that M is simple, which means that the empty set is a flat and the
rank one flats are exactly all singleton sets {e}, e ∈ E. This is not a real restriction, as
any matroid has a simplification with an isomorphic lattice of flats. To simplify notation,
we omit the braces when referring to singleton flats, or when adding or deleting a single
element from a flat or matroid.
Three operations on matroids will be important. Given any flat F ∈ L(M ), the
contraction MF is the matroid with ground set E r F whose lattice of flats is {G r F |
G ∈ L(M ) and G ⩾ F }. (More precisely, since this may not be a simple matroid, we
can take its simplification.)
The localization M F is the matroid with ground set F whose lattice of flats is
{G ∈ L(M ) | G ⩽ F }. We can combine contraction and localization: for F ⩽ G, the
matroids (MF )GrF and (M G )F are isomorphic, and we denote them MFG . The reader
should beware that our notation is opposite to the one used in [EPW16], where MF
denoted the localization and M F denoted the contraction.
The third operation is deletion. In this paper we will only consider deleting a single
element e ∈ E. The deletion matroid M r e is a matroid on the set E r e whose lattice
of flats is
{F r e | F ∈ L(M )}.
Note that the localization M F can also be expressed as the iterated deletion of all elements
of E r F . However, in our formulas the two operations play a somewhat different role, so
we will keep the terminology separate.

the electronic journal of combinatorics 27(1) (2020), #P1.17

4

2.2

Kazhdan–Lusztig polynomials

In this section we define the Kazhdan–Lusztig polynomials of matroids, using an alternate
definition based on a result of Proudfoot, Xu and Young [PXY18].
For any integer n ⩾ 0, let Pal(n) ⊂ P
Z[t, t−1 ] be the set of all Laurent polynomials such
k
that f (t) = tn f (t−1 ). In other words, N
k=−N ak t lies in Pal(n) if and only if ak = an−k
for all k.
Lemma 2.1. For any f ∈ Z[t, t−1 ] and any d ⩾ 0, there exists a unique g ∈ Z[t, t−1 ] with
deg g < d/2 so that f + g ∈ Pal(d). If f ∈ Z[t] and deg f ⩽ d, then g ∈ Z[t].
Theorem 2.2 ([PXY18]). There is a unique family of polynomials PM (t) ∈ Z[t] defined
for all matroids M with the following properties:
(a) If rk M = 0 then PM (t) = 1.
(b) For all matroids of positive rank, the degree of PM (t) is strictly less than (rk M )/2.
(c) For all matroids M , the polynomial
ZM (t) :=

X

trk F PMF (t)

(4)

F ∈L(M )

is in Pal(rk M ).
P
Proof. Apply the lemma to f = F ∈L(M )r{∅} trk F PMF (t). The summand for the flat E
is trk E = trk M , while the summand for a proper flat F has degree smaller than rk F +
(crk F )/2 < rk M . So the whole sum has degree exactly rk M .
Remark 2.3. Examining this proof, we see that it proves slightly more: since f = trk M +
lower order terms, we must have PM (0) = 1. In particular if rk M ⩽ 2 we have PM (t) = 1.
The linear coefficient is also easy to see. Let d = rk(M ). The degree of trk F PMF (t) is
at most d − 2 when crk F > 1, so the coefficient of td−1 in f is |Ld−1 (M )|, the number of
coatoms. The coefficient of t in f is clearly |L1 (M )|, so the coefficient of t in PM (t) is
|Ld−1 (M )| − |L1 (M )|.
Remark 2.4. The polynomials PM (t) were originally defined a different way in [EPW16],
using an approach closer to the definition of classical Kazhdan–Lusztig polynomials (see
[Pro18], which uses a framework of Stanley to show the parallels between these two theories
and the theory of toric g-polynomials of polytopes). The polynomial ZM (t) defined by
(4) was defined in [PXY18], where it was shown to be palindromic. Lemma 2.1 implies
that our definition gives the same polynomials as the original one.
The following useful result can be proved easily using either our definition of Kazhdan–
Lusztig polynomials or the one from [EPW16].
Proposition 2.5 ([EPW16],Proposition 2.7). For any matroids M , M 0 we have
PM ⊕M 0 (t) = PM (t)PM 0 (t).
In particular, if M is a Boolean matroid, it is a direct sum of rank 1 matroids, so
PM (t) = 1.
the electronic journal of combinatorics 27(1) (2020), #P1.17

5

2.3

The τ -invariant

Definition 2.6. For a matroid M whose rank is odd, say rk(M ) = 2k + 1, let τ (M ) be
the coefficient of tk in PM (t), in other words the coefficient of highest possible degree. If
rk(M ) is even, we put τ (M ) = 0.
The role that the invariant τ (M ) plays in our results about Kazhdan–Lusztig polynomials of matroids is analogous to the role the number µx,y plays in the classical theory
of Kazhdan–Lusztig polynomials of Coxeter groups. Unlike µx,y , however, τ (M ) seems to
very rarely vanish. The next lemma gives one important case when τ (M ) = 0.
Lemma 2.7. If M , M 0 are matroids of positive rank, then
τ (M ⊕ M 0 ) = 0.
Proof. The result is trivial if rk(M ⊕ M 0 ) is even, so we can suppose without loss of
generality that rk(M ) = 2k + 1 is odd and rk(M 0 ) = 2` is even. Then deg PM (t) ⩽ k
and deg PM 0 (t) ⩽ ` − 1, so τ (M ⊕ M 0 ), which is the coefficient of tk+` in PM ⊕M 0 (t) =
PM (t)PM 0 (t), must vanish.
2.4

Deletion formula

We are ready to state the main result of this paper. Let M be a simple matroid with
ground set E, and take e ∈ E. The deletion matroid M r e has as flats all sets F r e,
F ∈ L(M ).
Define a set
S := {F ∈ L(M ) | e ∈
/ F and F ∪ e ∈ L(M )}.

Theorem 2.8. If e ∈ E is not a coloop in M , then
X
PM (t) = PM re (t) − tPMe (t) +
τ (MF ∪e ) t(crk F )/2 PM F (t)

(5)

F ∈S

and
ZM (t) = ZM re (t) +

X

τ (MF ∪e ) t(crk F )/2 ZM F (t).

(6)

F ∈S

Note that since rk(F ∪ e) = rk(F ) + 1 whenever F ∈ S and τ (M ) = 0 if the rank of
M is even, either sum above can be replaced by the sum over all F ∈ S of even corank.
Example 2.9. Let us apply the theorem to the rank 1 uniform matroid on d+1 elements,
which we denote U1,d . For each k < d, its flats of rank k are all size k subsets of
E = {0, . . . , d}. In particular, every localization M F for F 6= E is Boolean, so PM F (t) = 1.
Deleting any element of E also results in a Boolean matroid, so PM re (t) = 1.
On the other hand, contracting an element results in a uniform matroid of smaller
rank: we have Me ∼
= U1,d−1 , and more generally MF ∪e ∼
= U1,d−k−1 , where k = |F |.
the electronic journal of combinatorics 27(1) (2020), #P1.17

6

Let ck1,d denote the coefficient of tk in PU1,d (t). For 0 < k < d/2 the degree k part of
the formula (5) gives


d
k−1
k
c1,d = −c1,d−1 +
ck−1 .
(7)
d − 2k 1,2k−1
A simple formula for ck1,d was established in [PWY16]: we have
ck1,d =







1
d−k−1 d+1
1
d−k
d+1
=
.
k+1
k
k
d−k k+1
k

(8)

Substituting this into (7) and rearranging, we have


 


1
d−k
d+1
d−k
d
k−1
k
c1,d + c1,d−1 =
+
d−k
k+1
k
k
k−1
(d − k − 1)! d!
(d − k)!d!
=
+
(k + 1)!(d − 2k − 1)!k!(d − k + 1)! k!(d − 2k)!(k − 1)!(d − k + 1)!
(d − k − 1)! d!
[(d + 1)(d − 2k) + k(k + 1)]
=
(d − k + 1)!(d − 2k)!(k + 1)!k!
(d − k − 1)! d!
=
(d − k)(d − k + 1)
(d − k + 1)!(d − 2k)!(k + 1)!k!
d!
=
(d − 2k)!(k + 1)!k!



d
2k
1
=
k d − 2k
k−1


d
=
ck−1 .
d − 2k 1,2k−1
Thus our formula gives a new proof of the formula (8), by induction on d. Similar formulas
for the coefficients of PUm,d (t) are given in [GLX+ ]. It may be possible to prove them using
our result, but we have not yet been able to do so.
Remark 2.10. The papers [PWY16, GPY17, GLX+ ] actually compute a richer invariant,
the equivariant Kazhdan–Lusztig polynomial, for uniform matroids. For a matroid with
an action of a finite group Γ, the coefficients of this polynomial are (virtual) characters of
Γ rather than integers. Since our formula requires choosing an element to delete and thus
breaks the symmetry, it cannot be refined to an equation of equivariant Kazhdan–Lusztig
polynomials for the full group that acts. However, it should be possible to upgrade it to
an equivariant formula for the action of the stabilizer of the element being deleted (we
thank the referee for pointing this out to us). It is possible that the extra structure this
gives would be helpful in computing PUm,d (t) for general m.

the electronic journal of combinatorics 27(1) (2020), #P1.17

7

2.5

Perverse elements and the KL basis

Let H = H(M ) be the free Z[t, t−1 ]-module with basis indexed by L(M ). In other words,
elements of H are formal sums
X
α=
αF · F, αF ∈ Z[t, t−1 ].
F ∈L(M )

There is an important abelian subgroup Hp ⊂ H, defined as the set of all α ∈ H so that
for every flat F ∈ L(M ) we have αF ∈ Z[t] and
X
trk F −rk G αG ∈ Pal(0).
(9)
G⩾F

Remark 2.11. We will not need this in what follows, but there is another way to describe
elements satisfying the condition (9). They are exactly the elements fixed by an involution
α 7→ α of H, defined by
X
α=
αF · F ,
F
−1

where αF (t) = αF (t ) and
F =

X

t2(rk G−rk F ) χMGF (t2 ) · G.

G⩽F

Here χM (t) denotes the characteristic polynomial of M .
For any flat F , define
ζF =

X
G

ζGF · G =

X

trk F −rk G PMGF (t−2 ) · G.

G⩽F

Lemma 2.12. ζ F lies in Hp .
Proof. Since deg PMGF (t2 ) < rk F − rk G unless F = G, we get that
X
ζF ∈ F +
tZ[t] · G,
G<F

so in particular ζGF ∈ Z[t] for all G.
To see that (9) holds, take any flat H ⩽ F . Then we have
X
X
trk H−rk G ζGF = trk F −rk H
(t−2 )rk G−rk H PMGF (t−2 )
H⩽G⩽F

G⩾H

= trk F −rk H

X

0

(t−2 )rk G PM F0 (t−2 )
G

F)
G0 ∈L(MH

= trk F −rk H ZMHF (t−2 ),
which lies in trk F −rk H · Pal(−2 rk MHF ) = Pal(0).
the electronic journal of combinatorics 27(1) (2020), #P1.17

8

Proposition 2.13. The elements ζ F , F ∈ L(M ) form a Z-basis for Hp . For any β ∈ Hp ,
we have
X
β=
βF (0)ζ F .
(10)
F

Proof. Since ζFF = 1 and ζGF = 0 unless G ⩽ F , the ζ F are linearly independent. To show
that they span, it is enough to show the formula (10). Take any β ∈ Hp , and let
X
α=β−
βF (0)ζ F .
F

We show that αF = 0 for all F , by induction on crk F . If we assume αG = 0 for all G > F ,
then the condition (9) says that αF ∈ Pal(0). Together with the facts that αF ∈ Z[t] and
αF (0) = 0, we immediately get αF = 0.
2.6

Deletion and the KL basis

Let M be a simple matroid and suppose e is not a coloop of M , so that M and M r e
have the same rank. We have a surjective map L(M ) → L(M r e) sending F to F r e.
For any flat F ∈ L(M ), define its discrepancy to be
δ(F ) = rkM (F ) − rkM re (F r e).
Define a homomorphism ∆ : H(M ) → H(M r e) by letting
∆(F ) = t−δ(F ) (F r e)
and extending Z[t, t−1 ]-linearly. Our main theorem will be a consequence of the following.
Proposition 2.14. We have ∆(ζ E ) ∈ Hp (M r e).
Proof. Let
β=

X

βG · G = ∆(ζ E ).

G∈L(M re)
E

P

Since ζ ∈ E + F 6=E tZ[t] · F , δ(F ) ∈ {0, 1} for every F , and δ(E) = 0 because e is not
a coloop, it follows that βG ∈ Z[t] for every G.
Now take a flat H of M r e, and consider the sum
X
X
X
trk H−rk G βG =
trk H−rk(F re) tδ(F ) ζFE =
trk H−rk F ζFE .
G∈L(M re)
G⩾H

F ∈L(M )
F re⩾H

F ∈L(M )
F re⩾H

Applying the following lemma now shows that this sum is in Pal(0).
Lemma 2.15. For any flat H ∈ L(M r e) and any F ∈ L(M ) we have F r e ⩾ H if and
only if F ⩾ H̄, where H̄ is the closure of H in M . Furthermore, we have
rkM H̄ = rkM re H.
Proof. If F ⩾ H̄, then F r e ⩾ H̄ r e = H. Conversely, if F r e ⩾ H, then F ⩾ F r e ⩾
H.
the electronic journal of combinatorics 27(1) (2020), #P1.17

9

2.7

Proof of Theorem 2.8, first part

Define β = ∆(ζ E ). Then Propositions 2.13 and 2.14 imply that
X
β=
βF (0)ζ F .

(11)

F ∈L(M re)

We have βEre (0) = ζEE (0) = 1. The only other way a summand of (11) can be nonzero is
if F = G r e for some flat G of M where δ(G) = 1, or in other words F ∪ e is in the set
S of Theorem 2.8. If that happens, we have
βF (0) = coefficient of t in ζFE∪e = τ (MF ∪e ).
In other words, we have
β = ζ Ere +

X

τ (MF ∪e )ζ F .

(12)

F ∈S

Now look at the coefficient of the empty flat in (12). By definition of β = ∆(ζ E ), we
have
β∅ = ζ∅E + t−1 ζeE
= trk E PM (t−2 ) + t−1 trk(Ere)−rk e PMe (t−2 )
= trk M (PM (t−2 ) + t−2 PMe (t−2 )).
On the other hand, we have
β∅ = ζ∅Ere +

X

τ (MF ∪e )ζ∅F

F ∈S
rk(Ere)

=t

PM re (t−2 ) +

X

τ (MF ∪e )trk F PM F (t−2 )

F ∈S

!
= trk M

PM re (t−2 ) +

X

t− crk F τ (MF ∪e )PM F (t−2 ) .

F ∈S

The first part of Theorem 2.8 follows.
2.8

Proof of Theorem 2.8, second part

To prove that the second equation of Theorem 2.8 holds, it will be useful to consider the
Z[t, t−1 ]-module map ΦM : H(M ) → Z[t, t−1 ] given by
X
ΦM (α) =
t− rk F αF .
F ∈L(M )

Then we have
ΦM re ◦ ∆ = ΦM ,
the electronic journal of combinatorics 27(1) (2020), #P1.17

10

which can be easily checked on the basis elements F ∈ L(M ).
Furthermore, for any flat F ∈ L(M ), we have
X
ΦM (ζ F ) =
trk F −2 rk G PMGF (t−2 )
G⩽F
rk F

=t

ZM F (t−2 ).

Now apply this to β = ∆(ζ E ). We get
ΦM re (β) = ΦM (ζ E ) = trk M ZM (t−2 ).
On the other hand, by (12), we have
ΦM re (β) = trk(M re) ZM re (t−2 ) +

X

τ (MF ∪e )trk(F ) ZM F (t−2 ).

F ∈S

Putting these two equalities together and dividing by trk M = trk(M re) gives the desired
equation (6) with t−2 in place of t.

3

Applications to graphic matroids

A graph G = (V, E) gives rise to a matroid MG on the ground set E, whose independent
sets are subsets of E containing no cycles. The rank of a set S ⊂ E of edges is
|V | − |connected components of the graph (V, S)|,
and its closure is
S = {e = {x, y} ∈ E | x and y are connected by a path in S} .
A set F of edges is a flat if F = F , or equivalently, if whenever all but one edge from a
cycle of G lies in F , the remaining edge is in F as well.
For a graph G, we put PG (t) = PMG (t) for the Kazhdan–Lusztig polynomial of the
associated matroid, and likewise we define τ (G) = τ (MG ). For example, the matroid of
an n-cycle is MCn = U1,n−1 , so by (8) its Kazhdan–Lusztig polynomial is
b(n−1)/2c

PCn (t) =

X
i=0


 
1
n−i−2 n i
t.
i+1
i
i

Not surprisingly, deletion and contraction for matroids corresponds to deleting and
contracting edges: we have MG r e = MGre and MG /e = (MG )e = MG/e . Note, however,
that contracting e can result in parallel vectors in MG /e, corresponding to the version
of edge contraction in which multiple edges are allowed. Since parallel vectors do not
affect the lattice of flats, it is convenient to identify any multiple edges resulting from a
contraction; this corresponds to taking the simplification of the matroid MG /e.
the electronic journal of combinatorics 27(1) (2020), #P1.17

11

3.1

Parallel connection graphs

In this section we describe a class of graphs for which our deletion formula becomes
particularly simple.
Definition 3.1. We say that a graph G is the parallel connection of subgraphs H1 and
H2 if H1 ∪ H2 = G and H1 ∩ H2 is a single edge e together with its vertices. If this holds,
the edge e is called the connection edge.
Note that these properties imply that H1 and H2 are vertex-induced subgraphs of G.
Theorem 3.2. Suppose that is G is the parallel connection of subgraphs H1 and H2 with
connection edge e, and H1 r e, H2 r e are both connected. Then
PG (t) = PGre (t) − tPH1 /e (t)PH2 /e (t).
Proof. Applying Theorem 2.8 we get
PG (t) + tPG/e (t) = PGre (t) +

X

τ (G/(F ∪ e))PF (t).

F ∈S

The graph G/e is isomorphic to the union of H1 /e and H2 /e joined at a vertex, so it has
the same matroid as the disjoint union of H1 /e and H2 /e, namely MH1 /e ⊕ MH2 /e . So by
Proposition 2.5 we have PG/e (t) = PH1 /e (t)PH2 /e (t).
Thus our result will follow if we can show that τ (G/(F ∪ e)) = 0 whenever F ∈ S. Let
Ei be the set of edges of Hi , and set Fi = F ∩Ei for i = 1, 2. Then G/(F ∪e) is isomorphic
to the union of H1 /(F1 ∪ e) and H2 /(F2 ∪ e) at a vertex, so unless F1 ∪ e or F2 ∪ e is the
entire edge set of H1 , H2 respectively, Lemma 2.7 implies that τ (G/(F ∪ e)) = 0. But if
Fi = Ei r e, then the endpoints of e are already connected by edges in F , so F is not a
flat.
Remark 3.3. If G is the parallel connection of H1 and H2 with connection edge e, the
matroid MG is a parallel connection matroid Par(MH1 , MH2 ), as defined in [Bry71],
for instance. The properties used in the proof of Theorem 3.2 still hold in this more
general context. For instance, Par(M1 , M2 )/e = (M1 /e) ⊕ (M2 /e) and Par(M1 , M2 )/d =
Par(M1 /d, M2 ) if d ∈ E(M1 ) r e. So the same proof gives the more general formula
PM (t) = PM re (t) − tPM1 /e (t)PM2 /e (t)
whenever M = Par(M1 , M2 ) is a parallel connection matroid with connection element e
and M1 r e, M2 r e are connected.
Example 3.4. Consider a double-cycle graph Cm,n obtained as the parallel connection
of an m-cycle and an n-cycle.
If e is the connection edge, then Cm,n r e ∼
= Cm+n−1 . So Theorem 3.2 gives
PCm,n (t) = PCm+n−2 (t) − tPCm−1 (t)PCn−1 (t),
the electronic journal of combinatorics 27(1) (2020), #P1.17

12

C6

e

C5

Figure 1: A double-cycle graph C6,5 .
and thus the coefficient of tk in PCm,n (t) is



m+n−k−4 m+n−2
1
k+1
k
k





X
1
n−i−3 n−1 m−j−3 m−1
−
.
(i + 1)(j + 1)
i
i
j
j
i+j=k−1
3.2

Example: partial saw graphs

More generally, Theorem 3.2 can be used to compute the Kazhdan–Lusztig polynomials of
an iterated parallel connection of any number of cycles, or equivalently any planar graph
obtained from a cycle by adding a set of non-crossing diagonals. We illustrate this for two
families of examples. For n ⩾ 3 and 0 ⩽ r ⩽ n, define a partial saw graph Sn,r to be
a graph obtained by forming an iterated parallel connection with r ⩽ n three-cycles at r
different edges of an n-cycle. Alternatively, it is an (n+r)-cycle with r noncrossing chords
added joining vertices at distance two. See Figure 2. Note that while this can describe
several different non-isomorphic graphs, all such graphs have isomorphic matroids. We
extend this to n = 2 by letting a 2-cycle be a single edge (or a pair of parallel edges,
which has the same lattice of flats), so S2,1 = C3 and S2,2 is the parallel connection of two
3-cycles.

Figure 2: A partial saw graph S6,4 .
For r > 0, let us apply Theorem 3.2 to Sn,r , which we consider as the parallel connection of Sn,r−1 and C3 . Let e be the connection edge, so e is on the central n-cycle
the electronic journal of combinatorics 27(1) (2020), #P1.17

13

and is not on any of the other 3-cycles. It is easy to see that Sn,r r e ∼
= Sn+1,r−1 and
∼
Sn,r−1 /e = Sn−1,r−1 , so our Theorem gives the following recursive formula:
PSn,r (t) = PSn+1,r−1 (t) − tPSn−1,r−1 (t)PC3 /e (t) = PSn+1,r−1 (t) − tPSn−1,r−1 (t),
valid for n ⩾ 3, r ⩾ 1. In order to make the formula hold for n = 1, 2 we can define
PS1,0 (t) = PS1,1 (t) = 0, and PS0,0 (t) = t−1 .
We can solve this recursion starting with Sn,0 = Cn to get the following general formula:
Theorem 3.5. We have
r
X

 
r
PSn,r (t) =
pn+r−2k (t),
(−t)
k
k=0
k

where pm (t) = PCm (t) for m ⩾ 2 and p1 (t) = 0, p0 (t) = t−1 .
For example, we have
 
 
3
2 3
PS3,3 (t) = PC6 (t) − t
PC4 (t) + t
PC2 (t) − t3 · t−1
1
2
= 1 + 9t + 5t2 − 3t(1 + 2t) + 3t2 − t2
= 1 + 6t + t2 .
The sequence of numbers τ (Sk,k ) is the sequence of “Motzkin sums” ([OEI, sequence
A00504]).
3.3

Fan graphs

For our second application of Theorem 3.2, we give a simpler proof of a formula of Liu, Xie
and Yang [LXY] for the Kazhdan–Lusztig polynomials of fan graphs. For n ⩾ 1, the fan
graph Fn is a graph with n + 1 vertices {0, 1, 2, . . . , n} and with edges (0, i) for 1 ⩽ i ⩽ n
and (i, i + 1) for 1 ⩽ i ⩽ n − 1. Thus F1 is a single edge, F2 ∼
= C3 , and F3 ∼
= K4 r e.
Theorem 3.6 ([LXY]). We have
c
b n−1
2



1
n−1
.
PFn (t) =
k + 1 k, k, n − 2k − 1
k=0
X

(13)

In order to apply Theorem 3.2 to compute PFn (t), we need to consider a larger class
of graphs. Let Fn,r be Fn with edges (0, n − r), . . . , (0, n − 1) deleted. Thus Fn,0 = Fn
and Fn,n−2 ∼
= Cn+1 . For any 0 ⩽ r ⩽ n − 3, the graph Fn,r is the parallel connection
of Fn−r−1 and a copy of Cr+3 with connection edge e = (0, n − r − 1). Furthermore,
Fn−r−1 /e ∼
= Fn−r−2 and Fn,r r e ∼
= Fn,r+1 , so Theorem 3.2 implies
PFn,r+1 (t) − PFn,r (t) = tPCr+2 (t)PFn−r−2 (t).
the electronic journal of combinatorics 27(1) (2020), #P1.17

14

Adding this equation for 0 ⩽ r ⩽ n − 3, and putting k = r + 2, we get
PFn (t) = PCn+1 (t) − t

r−1
X

PCk (t)PFn−k (t).

(14)

k=2

To solve this recursion, consider the generating series
X
X
ΦC (t, u) :=
PCn+1 (t)un , ΦF (t, u) :=
PFn (t)un .
n⩾1

n⩾1

Then summing un times the equation (14) gives
ΦF (t, u) = ΦC (t, u) − tu ΦC (t, u)ΦF (t, u),

(15)

so the series ΦF and ΦC determine each other.
In [LXY] it is explained that the formula (13) is equivalent to
2u
p
1 − u + (1 − u)2 − 4tu2
i
p
1 h
1 − u − (1 − u)2 − 4tu2 .
=
2tu

ΦF (t, u) =

(Note that this formula differs from the one in [LXY] because our sum for ΦF (t, u) starts
at n = 1 instead of n = 0.)
Plugging this into (15), we have
ΦF (t, u)
1 − tuΦF (t, u)
h
i
p
1
2 − 4tu2
1
−
u
−
(1
−
u)
2tu
i
h
=
p
1
1 − tu 2tu
1 − u − (1 − u)2 − 4tu2
p
1 1 − u − (1 − u)2 − 4tu2
p
=
·
tu 1 + u + (1 − u)2 − 4tu2
p
1 1 − u2 − 2 (1 − u)2 − 4tu2 + (1 − u)2 − 4tu2
=
·
tu
(1 + u)2 − (1 − u)2 + 4tu2
p
1 − u − 2tu2 − (1 − u)2 − 4tu2
=
.
2tu2 (1 + tu)

ΦC (t, u) =

This agrees with the formula for ΦC (t, u) given in [PWY16], where it is also shown that
this formula is equivalent to the formula (8) for the coefficients of PCn+1 (t). Thus we
obtain a self-contained proof of Theorem 3.6 using Theorems 2.8 and 3.2.

the electronic journal of combinatorics 27(1) (2020), #P1.17

15

Remark 3.7. It is easy to see that the coefficient
 of t in the Kazhdan–Lusztig polynomial
n
of an n-cycle with k non-crossing edges is k − n − k, so in particular it is independent
of the edges chosen (if the diagonals are allowed to cross, however, this is no longer
true). However, Theorem 3.6 gives PF5 (t) = 1 + 6t + 2t2 , and we have already seen that
PS3,3 (t) = 1 + 6t + t2 . These are both triangulations of 6-cycles, so this shows that the
quadratic coefficient is sensitive to the arrangement of diagonals.
3.4

A thagomizer lemma

We finish with one more simple application of Theorem 2.8. Each of our applications has
relied on some simplification of the potentially complicated sum on the right side of (5).
The application to uniform matroids U1,d used two facts: (1) flats of a given rank are easy
to count and (2) for each proper flat F the localization M F is Boolean, so PM F (t) = 1.
On the other hand, in Theorem 3.2 all the numbers τ (MF ∪e ) = 0, so all terms in the sum
vanish.
Now, we give a situation in which the formula is simple because the set S that is
summed over is very small. Let e be an edge of a graph G, and suppose that G contains
a triangle with edges e, e0 , e00 . A flat in L(MG ) cannot contain exactly two of these edges
of the triangle, and so a flat F that is in S cannot contain any edge of the triangle.
We apply this observation to the thagomizer graph Tn considered in [Ged17]. This is
a graph obtained from a complete bipartite graph K2,n by adding a single edge e joining
the two vertices in the first part. Every edge of Tn is part of a triangle containing e,
and so by the previous paragraph, if we apply our deletion formula to the edge e, the set
S contains only the empty flat ∅. Furthermore, the summand corresponding to this flat
vanishes, because G/e is a tree and so τ (G/e) = 0. Thus we obtain the following result.
Lemma 3.8 ([GPY17, Theorem 5.8]). PTn (t) = PK2,n (t) − t.
Acknowledgements
The authors thank Jacob Matherne and Nicholas Proudfoot for helpful suggestions on
a draft of this paper, and the anonymous referee for numerous corrections and improvements.

References
[Bry71]

Thomas H. Brylawski, A combinatorial model for series-parallel networks,
Trans. Amer. Math. Soc. 154 (1971), 1–22.

[EPW16] Ben Elias, Nicholas Proudfoot, and Max Wakefield, The Kazhdan-Lusztig polynomial of a matroid, Adv. Math. 299 (2016), 36–70.
[Ged17]

Katie R. Gedeon, Kazhdan-Lusztig polynomials of thagomizer matroids, Electron. J. Combin. 24 (2017), no. 3, Paper 3.12, 10.

the electronic journal of combinatorics 27(1) (2020), #P1.17

16

[GLX+ ]

Alice L. L. Gao, Linyuan Lu, Matthew H. Y. Xie, Arthur L. B. Yang,
and Philip B. Zhang, The Kazhdan-Lusztig polynomials of uniform matroids,
preprint arXiv:1806.10852.

[GPY17] Katie Gedeon, Nicholas Proudfoot, and Benjamin Young, The equivariant
Kazhdan-Lusztig polynomial of a matroid, J. Combin. Theory Ser. A 150
(2017), 267–294.
[Hum90] James E. Humphreys, Reflection groups and Coxeter groups, Cambridge Studies
in Advanced Mathematics, vol. 29, Cambridge University Press, Cambridge,
1990.
[KL79]

David Kazhdan and George Lusztig, Representations of Coxeter groups and
Hecke algebras, Invent. Math. 53 (1979), no. 2, 165–184.

[LXY]

Linyuan Lu, Matthew H. Y. Xie, and Arthur L. B. Yang, Kazhdan-Lusztig
polynomials of fan matroids, wheel matroids and whirl matroids, preprint
arXiv:1802.03711.

[OEI]

The on-line encyclopedia of integer sequences, published electronically at
https://oeis.org.

[Pro18]

Nicholas Proudfoot, The algebraic geometry of Kazhdan-Lusztig-Stanley polynomials, EMS Surv. Math. Sci. 5 (2018), no. 1, 99–127.

[PWY16] Nicholas Proudfoot, Max Wakefield, and Ben Young, Intersection cohomology
of the symmetric reciprocal plane, J. Algebraic Combin. 43 (2016), no. 1, 129–
138.
[PXY18] Nicholas Proudfoot, Yuan Xu, and Ben Young, The Z-polynomial of a matroid,
Electron. J. Combin. 25 (2018), #P1.26.

the electronic journal of combinatorics 27(1) (2020), #P1.17

17

