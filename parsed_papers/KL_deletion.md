Notes: Inverse Kazhdan-Lusztig Polynomials under Deletion

1

June 22, 2025

Introduction

The Kazhdan-Lusztig polynomial PM (t) is a fundamental invariant associated with any matroid M , as defined by Elias, Proudfoot, and Wakefield in [2]. This polynomial, denoted PM (t), exhibits formal similarities
to the Kazhdan-Lusztig polynomials defined for Coxeter groups. The coefficients of PM (t) depend only on
the lattice of flats L(M ) of the matroid, and in fact, they are integral linear combinations of the flag Whitney
numbers counting chains of flats with specified ranks.
In [1], Braden and Vysogorets presented a formula that relates the Kazhdan-Lusztig polynomial of a matroid
M to that of the matroid obtained by deleting an element e, denoted M \ e, as well as various contractions
and localizations of M . Specifically, for a simple matroid M where e is not a coloop, their main result,
Theorem 2.8, states:
X
PM (t) = PM \e (t) − tPMe (t) +
τ (MF ∪e ) · tcrk(F )/2 · PM F (t)
F ∈S

where the sum is taken over the set S of all subsets F of E \ e such that both F and F ∪ e are flats of M ,
and τ (M ) is the coefficient of t(rk(M )−1)/2 in PM (t) if rk(M ) is odd, and zero otherwise.
The inverse Kazhdan-Lusztig polynomial QM (x) is another important invariant. There is a related polynomial Q̂M (x) = (−1)rk(M ) QM (x) which acts as the inverse of the Kazhdan-Lusztig polynomial PM (t) within
the incidence algebra of the lattice of flats L(M ).
In this paper, we aim to prove the following deletion formula for Q̂M (x):
Theorem 1 (Deletion Formula for Q̂M (x)). Let M be a simple matroid and e an element that is not a
coloop. Then
X
Q̂M (x) = Q̂M \e (x) − (1 + x) · Q̂Me (x) −
τ (MeG ) · xrk(G)/2 · Q̂MG (x)
G∈S ′
′

where S = {F ∈ L(M ) | e ∈ F and F \ e ∈
/ L(M )}.
The proof of this theorem is the main goal of these notes.

2

Perverse elements and the KL basis

Let M be a matroid and L(M ) be its lattice of flats.
• The Module H(M ): Let H = H(M ) be the free Z[t, t−1 ]-module with basis indexed by L(M ).
Elements of H are formal sums of the form
X
α=
αF · F, αF ∈ Z[t, t−1 ].
F ∈L(M )

• The Abelian Subgroup Hp : Hp is an abelian subgroup of H consisting of all α ∈ H such that
for every flat F ∈ L(M ), the following two conditions hold:
i. αF ∈ Z[t].
P
rk(F )−rk(G)
ii.
αG ∈ P al(0), where P al(0) is the set of Laurent polynomials f (t) such that
G≥F t
f (t) = f (t−1 ).
• The Elements ζ F : For any flat F ∈ L(M ), an element ζ F ∈ H is defined as
X
ζF =
trk(F )−rk(G) PMGF (t−2 ) · G.
G≤F

1

• Basis of Hp : Proposition 2.13 of [1] states that the set of elements {ζ F }F ∈L(M ) forms a Z-basis for
Hp . Any element β ∈ Hp can be uniquely expressed as a linear combination of the ζ F with integer
coefficients:
X
β=
βF (0)ζ F .
F ∈L(M )

This algebraic framework, involving the module H(M ) and its subgroup Hp with the basis {ζ F }, provides
a foundation for studying the Kazhdan–Lusztig polynomials of matroids, as demonstrated by its role in the
derivation of deletion formulas.

3

The module homomorphism H(M ) → H(M \ e)

Let M be a simple matroid and e be an element of its ground set that is not a coloop. There is a surjective map
L(M ) → L(M \ e) sending a flat F ∈ L(M ) to F \ e ∈ L(M \ e). There also exists a module homomorphism
∆ : H(M ) → H(M \ e) which is Z[t, t−1 ]-linear and is defined on the basis elements F ∈ L(M ) by


if F ̸∋ e
F
∆(F ) = F \ e
if F ∋ e and F \ e ∈
/ L(M )

 −1
t · (F \ e) if F ∋ e and F \ e ∈ L(M ).
This definition is taken from Section 2.6 of Braden and Vysogorets [1]. In [1], the authors also prove the
following lemma:
Lemma 2. Let F ∈ L(M ) be a flat such that e ∈ F and F \ e ∈
/ L(M ). Then
X
F
∆(ζ F ) = ζ F \e +
τ (MG∪e
) · ζG
G∈S(M F )

where S(M F ) = {G ∈ L(M F ) | e ∈
/ G and G ∪ e ∈ L(M F )}.
Theorem 3. Let F ∈ L(M ) be a flat such that e ∈ F and F \ e ∈ L(M ), then
∆(ζ F ) = (t + t−1 )ζ F \e
where ζ F \e on the right-hand side is the ζ-element in H(M \ e) associated with the flat F \ e ∈ L(M \ e).
Proof. Let F0 = F \ e. We are given F0 ∈ L(M ). By the definition of ∆(G):
• If G ≤ F and e ∈
/ G: Then G ≤ F0 . Since G ∈ L(M ) and e ∈
/ G, G is also a flat in M \ e, so
G ∈ L(M \ e). In this case, ∆(G) = G.
• If G ≤ F and e ∈ G: Let G0 = G \ e. Then G0 ≤ F0 . Since F0 ∈ L(M ), it follows that G0 = G ∩ F0 ∈
L(M ). Thus G0 ∈ L(M \ e). In this case, ∆(G) = t−1 G0 .
Applying this to ∆(ζ F ):

∆(ζ F ) = ∆ 


X

trkM (F )−rkM (G) PMGF (t−2 ) · G

G≤F

X

=

trkM (F )−rkM (G) PMGF (t−2 ) · ∆(G)

G≤F,G̸∋e

X

+

trkM (F )−rkM (G) PMGF (t−2 ) · ∆(G)

G≤F,G∋e

=

X

trkM (F )−rkM (G) PMGF (t−2 ) · G

G≤F0

+

X

trkM (F )−rkM (G0 ∪{e}) PM F

G0 ∪{e}

G0 ≤F0
(G=G0 ∪{e})

2

(t−2 ) · (t−1 G0 ).

We use the rank relations:
• rkM (F ) = rkM \e (F0 ) + 1.
• For G ≤ F0 : rkM (G) = rkM \e (G).
• For G0 ≤ F0 : rkM (G0 ∪ {e}) = rkM \e (G0 ) + 1.
And the Kazhdan-Lusztig polynomial identities under these conditions:
F ∼
−2
0
F (t
• For G ≤ F0 : MG
) = P(M \e)F0 (t−2 ).
= (M \ e)F
G ⊕ U1,1 ({e}), so PMG
G

•

F
0
∼
F
(t−2 ) = P(M \e)F0 (t−2 ).
For G0 ≤ F0 : MG
= (M \ e)F
G0 , so PMG
0 ∪{e}
G
0 ∪{e}
0

Substituting these into the sums:
X
t(rkM \e (F0 )+1)−rkM \e (G) P(M \e)F0 (t−2 ) · G
∆(ζ F ) =
G

G≤F0

+ t−1

X

t(rkM \e (F0 )+1)−(rkM \e (G0 )+1) P(M \e)F0 (t−2 ) · G0
G0

G0 ≤F0

X

=t

trkM \e (F0 )−rkM \e (G) P(M \e)F0 (t−2 ) · G
G

G≤F0 ,G∈L(M \e)

X

+ t−1

trkM \e (F0 )−rkM \e (G0 ) P(M \e)F0 (t−2 ) · G0 .
G0

G0 ≤F0 ,G0 ∈L(M \e)
F0
Using the definition of ζM
\e :
F0
F0
−1
∆(ζ F ) = t · ζM
· ζM
\e + t
\e
F0
= (t + t−1 )ζM
\e .

4

The Deletion Formula for Q̂M (x)

Lemma 4. The standard basis {F }F ∈L(M ) of H(M ) satisfies
F =

X

trk(F )−rk(G) Q̂MGF (t−2 ) · ζ G .

(1)

G≤F

Proof of 1. Applying the homomorphism ∆ to equation 1 when F = E, we get
X
E\e=
trk(E)−rk(G) Q̂MGE (t−2 ) · ∆(ζ G ).
G≤E

Using lemma 4, the coefficient of ζ ∅ in the left-hand side is trk(E\e)−rk(∅) · Q̂M E\e (t−2 ) = trk(M ) · Q̂M \e (t−2 ).
∅

∅

By Theorem 3, the coefficient ζ on the right-hand side is non-zero only when G ∈ {∅, e} ∪ S ′ . In each of
these cases, we have the following:
• For G = ∅, we have ∆(ζ ∅ ) = ζ ∅ .
• For G = e, we have ∆(ζ e ) = (t + t−1 )ζ ∅ .
• For G ∈ S ′ , we have ∆(ζ G ) = τ (MeG ) · ζ ∅ + terms not including ζ ∅ .

3

Collecting the coefficients of ζ ∅ on the right-hand side, we have:
X

trk(E)−rk(∅) Q̂M E (t−2 ) + trk(E)−rk(e) (t + t−1 )Q̂MeE (t−2 ) +
∅

trk(E)−rk(G) Q̂MGE (t−2 ) · τ (MeG )

G∈S ′

= trk(M ) Q̂M (t−2 ) + trk(M )−1 (t + t−1 )Q̂Me (t−2 ) +

X

trk(M )−rk(G) Q̂MG (t−2 ) · τ (MeG ).

G∈S ′

Equating the coefficients of ζ ∅ on both sides, we obtain:
Q̂M \e (t−2 ) = Q̂M (t−2 ) + (1 + t−2 )Q̂Me (t−2 ) +

X

t−rk(G) Q̂MG (t−2 ) · τ (MeG ).

G∈S ′

Finally, taking x = t−2 and rearranging yields the desired statement:
X
Q̂M (x) = Q̂M \e (x) − (1 + x) · Q̂Me (x) −
τ (MeG ) · xrk(G)/2 · Q̂MG (x).
G∈S ′

The inverse Kazhdan-Lusztig polynomial QM (x) = (−1)rk(M ) Q̂M (x) then satisfies the following:
Corollary 5. Let M be a simple matroid and e an element that is not a coloop. Then
X
QM (x) = QM \e (x) + (1 + x) · QMe (x) −
τ (MeG ) · xrk(G)/2 · QMG (x)
G∈S ′

where S ′ = {F ∈ L(M ) | e ∈ F and F \ e ∈
/ L(M )}.
Corollary 6. Let M := Um,d be the uniform matroid of rank d on m + d elements with d ≥ 1. Then
QUm,d (x) = QUm−1,d (x) + (1 + x) · QUm,d−1 (x) − τ (Um,d−1 ) · xd/2 .
Proof. As none of the elements in the ground set are coloops, we may apply the deletion formula for a generic
element e in the ground set. The set S ′ then consists only of the top flat E and the sum over S ′ reduces to
τ (Me ) · xrk(M )/2 = τ (Um,d−1 ) · xd/2 .

♣ Jacob: [For the previous corollary, can you now use induction to get a formula for Qm,d for any m and d that
does not have any Q’s in it? (Perhaps starting with the fact the inverse KL polynomials of Boolean matroids are
equal to 1?)]
Corollary 7. Let M be the parallel connection of the cycle matroids U1,m and U1,n along the element e.
Then
QM (x) = QU1,m+n−1 (x) + (1 + x) · QU1,m−1 (x) · QU1,n−1 (x)
h
i
− τ (U1,n−1 ) · xm/2 · QU1,m−1 (x) + τ (U1,m−1 ) · xn/2 · QU1,n−1 (x) + τ (Me ) · x(m+n−1)/2 .
Specifically, when the ranks m and n are odd, the τ terms are 0 and hence the formula simplifies to:
QM (x) = QU1,m+n−1 (x) + (1 + x) · QU1,m−1 (x) · QU1,n−1 (x).
♣ Nutan: [Corrected an error in the statement of above corollary.]

4

Corollary 8. Let M = P G(r − 1, q) be the projective geometry of rank r over the finite field GF (q), for
r ≥ 2. Then the deletion formula for its inverse Kazhdan-Lusztig polynomial is:


r−1
QM (x) = QM \e (x) + (1 + x) · QP G(r−2,q) (x) −
· x · QP G(r−3,q) (x)
1 q


r−1
r−1
where
= q q−1−1 is the number of lines through the point e in M .
1 q
Proof. We start from the formula for QM (x) in Corollary 5 and substitute M = P G(r − 1, q). The lattice of
flats of a projective geometry is modular. For any matroid N with a modular lattice of flats, its KazhdanLusztig polynomial PN (t) is 1. [3][Proposition 2.14] The coefficient τ (N ) is the coefficient of t(rk(N )−1)/2 in
PN (t), which is zero if rk(N ) ≥ 2.
The sum in Corollary 5 is over the set S ′ = {G ∈ L(M ) | e ∈ G and G \ e ∈
/ L(M )}. For the projective
geometry M , a flat G containing e is a linear subspace. If rk(G) ≥ 2, removing the point e results in a set
G \ e that is not a subspace, and thus not a flat. If rk(G) = 1, then G = {e} and G \ e = ∅, which is a flat.
Thus, for M = P G(r − 1, q), the set S ′ consists of all flats containing e of rank 2 or greater.
For each G ∈ S ′ , the term in the sum is τ (MeG ) · xrk(G)/2 · QMG (x). The matroid MeG is the interval [e, G]
isomorphic to P G(k − 2, q) where k = rk(G). The rank of MeG is k − 1 and τ (MeG ), therefore, is non-zero
only if the rank k − 1 = 1, which implies k = 2.
Thus, the sum is over the set of rank-2 flats containing the point e. The number of such flats is the number of
2-dimensional subspaces of V (r, q) containing a given 1-dimensional subspace, which is equal to
number
 the 
r
−
1
. For
of 1-dimensional subspaces in the quotient space V (r, q)/⟨e⟩ ∼
= V (r − 1, q). This number is
1 q
each such rank-2 flat G:
• τ (MeG ) = τ (P G(0, q)) = 1 since P G(0, q) has rank 1.
• QMG (x) = QP G(r−3,q) (x), since the contraction MG of M = P G(r − 1, q) by a rank-2 flat G is
isomorphic to P G(r − 3, q).
The entire sum therefore reduces to:
X

τ (MeG ) · xrk(G)/2 · QMG (x) =

G∈S ′ ,rk(G)=2



r−1
· x · QP G(r−3,q) (x).
1 q

Substituting this and the fact that the contraction Me is isomorphic to P G(r − 2, q) back into the general
formula from Corollary 5, we get:


r−1
QP G(r−1,q) (x) = QM \e (x) + (1 + x) · QP G(r−2,q) (x) −
· x · QP G(r−3,q) (x).
1 q

Remark. The inverse Kazhdan-Lusztig polynomial of a projective geometry P G(k − 1, q) of rank k is known
k
to be the constant polynomial q (2) . This allows for substituting the known values for the Q polynomials in
the formula to obtain an explicit expression for QM \e (x). Rearranging the terms and substituting gives:


r−1
QM \e (x) = QP G(r−1,q) (x) − (1 + x)QP G(r−2,q) (x) +
x QP G(r−3,q) (x)
1 q
r
r−1
q
= q (2) − (1 + x)q ( 2 ) +

r−1

− 1 (r−2
q 2 ) · x.
q−1

5

References
[1]

Tom Braden and Artem Vysogorets. “Kazhdan–Lusztig polynomials of matroids under deletion”. In:
Electron. J. Combin. 27.1 (2020), P1.17.
[2] Ben Elias, Nicholas Proudfoot, and Max Wakefield. “The Kazhdan-Lusztig polynomial of a matroid”.
In: Adv. Math. 299 (2016), pp. 36–70.
[3] Ben Elias, Nicholas Proudfoot, and Max Wakefield. “The Kazhdan-Lusztig polynomial of a matroid”.
In: Adv. Math. 299 (2016), pp. 36–70. issn: 0001-8708. doi: 10 . 1016 / j . aim . 2016 . 05 . 005. url:
https://doi.org/10.1016/j.aim.2016.05.005.

6

