"""
Extension functions for matroid operations.

This module contains extended functionality for matroid operations that
are not available in the standard SageMath matroids module.
"""

from sage.all import *

def is_graphic(matroid):
    """
    Check if a matroid is graphic using excluded minors.
    
    This is a custom implementation that may be more reliable than
    the standard SageMath is_graphic function.
    
    INPUT:
    - matroid: a matroid
    
    OUTPUT:
    - Boolean indicating if the matroid is graphic
    """
    from sage.matroids.database_matroids import (
        U24,
        Fano,
        FanoDual,
        K5dual,
        K33dual
    )
    excluded_minors = [U24(), Fano(), FanoDual(), K5dual(), K33dual()]
    for M in excluded_minors:
        if matroid.has_minor(M):
            return False
    return True

def is_paving(M):
    """
    Check if a matroid is paving.
    
    A matroid is paving if every circuit has size at least equal to the rank.
    
    INPUT:
    - M: a matroid
    
    OUTPUT:
    - Boolean indicating if the matroid is paving
    """
    n = M.size()
    r = M.rank()
    return (len(M.independent_r_sets(r-1)) == binomial(n, r-1)) 