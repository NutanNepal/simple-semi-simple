"""
Polynomial functions for matroids.

This module contains custom implementations of various polynomial computations
for matroids, including characteristic polynomials, Kazhdan-Lusztig polynomials,
and Q-polynomials.
"""

from sage.all import *
from .core import characteristic_polynomial

# Global polynomial ring
R = PolynomialRing(QQ, 't')
t = R.gen()

def uniformQpoly(r, n):
    """
    Compute the Q-polynomial for uniform matroid U(r,n).
    
    INPUT:
    - r: rank of the uniform matroid
    - n: size of the groundset
    
    OUTPUT:
    - Q-polynomial as a polynomial in t
    """
    m, d = n-r, r
    upper_bound = (d-1)//2
    sum = R(0)
    for j in range(0, upper_bound + 1):
        coeff = m * (d - 2 * j)/((m + j) * (m + d - j)) * (binomial(d, j))
        sum = sum + coeff * t**(j)
    return binomial(m+d, d) * sum

def uniformKLpoly(r, n):
    """
    Compute the Kazhdan-Lusztig polynomial for uniform matroid U(r,n).
    
    INPUT:
    - r: rank of the uniform matroid
    - n: size of the groundset
    
    OUTPUT:
    - Kazhdan-Lusztig polynomial as a polynomial in t
    """
    m, d = n - r, r
    upper_bound = (d-1)//2
    sum = R(0)
    for i in range(0, upper_bound + 1):
        s = R(0)
        for h in range(0, m):
            s = s + binomial(d - i + h, h + i + 1) * binomial(i - 1 + h, h)
        s = s * binomial(m + d, i)/(d - i)
        sum = sum + s * t**(i)
    return sum

def kazhdan_lusztig_inverse_uniform(k, n):
    """
    Compute the inverse Kazhdan-Lusztig polynomial for uniform matroid U(k,n).
    
    INPUT:
    - k: rank of the uniform matroid
    - n: size of the groundset
    
    OUTPUT:
    - Inverse Kazhdan-Lusztig polynomial as a polynomial in t
    """
    if k == n:
        return R(1)
    d = k
    m = n - d
    ans = 0
    for j in range((d-1)//2 + 1):
        ans = ans + m * (d-2*j)/((m+j) * (m+d-j)) * binomial(d, j) * t**j
    return ans * binomial(m+d, d)

def q_kl(k, h):
    """
    Helper function for KL inverse computations.
    
    INPUT:
    - k: rank parameter
    - h: height parameter
    
    OUTPUT:
    - Difference of inverse KL polynomials
    """
    return kazhdan_lusztig_inverse_uniform(k, h+1) - kazhdan_lusztig_inverse_uniform(k-1, h)

def inverse_kazhdan_lustig_polynomial(M):
    """
    Compute inverse Kazhdan-Lusztig polynomial for a matroid.
    
    This is a fast implementation that works for uniform matroids
    and some other special cases.
    
    INPUT:
    - M: a matroid
    
    OUTPUT:
    - Inverse KL polynomial as a polynomial in t
    """
    if M.loops(): 
        return R(0)
    k, n = M.rank(), M.size()
    if k == n or k == 0: 
        return R(1)
    if not M.is_connected():
        ans = R(1)
        CC = M.components()
        for N in CC:
            res = M.delete(M.groundset() - N)
            ans = ans * inverse_kazhdan_lustig_polynomial(res)
        return ans

    from .extensions import is_paving
    if is_paving(M):
        return kl_inverse_paving(M)
    if is_paving(M.dual()):
        return kl_inverse_copaving(M)
    
    LF = M.lattice_of_flats()
    ans = R(0)
    for F in LF:
        if len(F) != n:
            Res = M.delete(M.groundset() - F)
            Con = M.contract(F)
            chi = characteristic_polynomial(Con)(1/t) * t**(Con.rank())
            PPP = inverse_kazhdan_lustig_polynomial(Res)(t) * (-1)**(Res.rank())
            ans = ans + chi * PPP
    assert (t**k * ans(1/t)).numerator() == -ans(t)
    ans = ans.numerator() * (-1)**(k+1)
    return ans.truncate((k+1)//2)

# Alias for backward compatibility and convenience
invkl = inverse_kazhdan_lustig_polynomial

def kl_inverse_paving(M):
    """
    Compute inverse KL polynomial for paving matroids.
    
    INPUT:
    - M: a paving matroid
    
    OUTPUT:
    - Inverse Kazhdan-Lusztig polynomial
    """
    from .extensions import is_paving
    assert is_paving(M)
    n = M.size()
    k = M.rank()
    ans = kazhdan_lusztig_inverse_uniform(k, n)
    for H in M.hyperplanes():
        h = len(H)
        if h >= k:
            ans = ans - q_kl(k, h)
    return ans

def kl_inverse_copaving(M):
    """
    Compute inverse KL polynomial for copaving matroids.
    
    INPUT:
    - M: a copaving matroid
    
    OUTPUT:
    - Inverse Kazhdan-Lusztig polynomial
    """
    from .extensions import is_paving
    assert is_paving(M.dual())
    n = M.size()
    k = M.rank()
    ans = kazhdan_lusztig_inverse_uniform(k, n)
    for H in M.dual().hyperplanes():
        h = len(H)
        if h >= n-k:
            ans = ans - kli_vtilde_dual(n-k, h, n) + kazhdan_lusztig_inverse_uniform(h-n+k+1, h) * kazhdan_lusztig_inverse_uniform(n-h-1, n-h)
    return ans

def kli_vtilde_dual(k, h, n):
    """
    Helper function for dual KL inverse computations.
    """
    return helper1(n-k, h, n)

def helper1(k, h, n):
    """
    Helper function for KL inverse computations.
    """
    c = n - h
    ans1 = kazhdan_lusztig_inverse_uniform(k, n)
    ans2 = helper2(c, k, n)
    ans3 = kazhdan_lusztig_inverse_uniform(k-c+1, h) * kazhdan_lusztig_inverse_uniform(c-1, c)
    return ans1 - ans2 + ans3

def helper2(c, k, n):
    """
    Helper function for KL inverse computations.
    """
    h = n - c
    ans = 0
    for j in range(k-c+1):
        ans = ans + binomial(n-c, j) * (-1)**(c-1+j) * kazhdan_lusztig_inverse_uniform(c-1, c) * t**(k-c-j+1) * chuly(k-c-j+1, n-c-j)(1/t)
    for i in range(c-1):
        for j in range(k-i):
            ans = ans + binomial(c, i) * binomial(n-c, j) * (-1)**(i+j) * t**(k-i-j) * helper4(c, k, n, i, j)(1/t)
    ans = ans.numerator().truncate((k-1)//2 + 1)
    if ans[0] < 0:
        ans = -ans
    return ans

def helper3(c, k, n):
    """
    Helper function for KL inverse computations.
    """
    ans = 0
    for j in range(k-c+1):
        ans = ans + binomial(n-c, j) * uniformKLpoly(c-1, c) * (-1)**(k-c-j+1) * kazhdan_lusztig_inverse_uniform(k-c-j+1, n-c-j)
    for i in range(c-1):
        for j in range(k-i):
            ans = ans + binomial(c, i) * binomial(n-c, j) * (-1)**(k-i-j) * helper2(c-i, k-i-j, n-i-j)
    return -ans

def helper4(c, k, n, i, j):
    """
    Helper function for KL inverse computations.
    """
    ans = 0
    for l in range(c-i-1):
        ans = ans + (-1)**l * (t-1)**(max(n-i-j-l-1, 0))
    for u in range(n-k-1):
        ans = doit_once(ans)
    return ans

def chuly(a, b):
    """
    Helper function for KL inverse computations.
    """
    ans = (t-1)**b
    for i in range(b-a):
        ans = doit_once(ans)
    return ans

def doit_once(p):
    """
    Helper function for KL inverse computations.
    """
    p = p // t**2
    p = p * t
    p = p - p(1)
    return p

def lorenzo(k, h, n):
    """
    Helper function for KL inverse computations.
    """
    c = n - h
    ans1 = uniformKLpoly(k, n) + uniformKLpoly(k-c+1, h) * uniformKLpoly(c-1, c)
    ans2 = helper3(c, k, n)
    return ans1 - ans2 