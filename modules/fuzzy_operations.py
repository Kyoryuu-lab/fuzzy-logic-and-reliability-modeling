"""
==============================================================================
Module:      fuzzy_operations.py
Description: Standard fuzzy set operations: Union (T-Conorm / Max),
             Intersection (T-Norm / Min), Complement (Negation / 1 - mu),
             and batch pairwise combination generators.
==============================================================================
"""

import numpy as np
from typing import Dict, Callable, Any


def fuzzy_union(val_a: float, val_b: float) -> float:
    """Standard-Vereinigung (S-Norm): max(mu_A, mu_B)"""
    return max(val_a, val_b)


def fuzzy_intersection(val_a: float, val_b: float) -> float:
    """Standard-Schnittmenge (T-Norm): min(mu_A, mu_B)"""
    return min(val_a, val_b)


def fuzzy_complement(val_a: float) -> float:
    """Standard-Komplement (Negation): 1 - mu_A"""
    return 1.0 - val_a


def compute_pairwise_unions(memberships: Dict[str, Callable[[float], float]],
                            step: int = 10, max_val: int = 100) -> Dict[str, Dict[int, float]]:
    """Berechnet die paarweise Vereinigung aller Terme diskretisiert ueber [0, max_val]."""
    results = {}
    terms = list(memberships.keys())
    for i in range(len(terms)):
        for j in range(i + 1, len(terms)):
            t1, t2 = terms[i], terms[j]
            fn1, fn2 = memberships[t1], memberships[t2]
            values = {x: round(fuzzy_union(fn1(x), fn2(x)), 4) for x in range(0, max_val + 1, step)}
            results[f"{t1} u {t2}"] = values
    return results


def compute_pairwise_intersections(memberships: Dict[str, Callable[[float], float]],
                                   step: int = 10, max_val: int = 100) -> Dict[str, Dict[int, float]]:
    """Berechnet die paarweise Schnittmenge aller Terme diskretisiert ueber [0, max_val]."""
    results = {}
    terms = list(memberships.keys())
    for i in range(len(terms)):
        for j in range(i + 1, len(terms)):
            t1, t2 = terms[i], terms[j]
            fn1, fn2 = memberships[t1], memberships[t2]
            values = {x: round(fuzzy_intersection(fn1(x), fn2(x)), 4) for x in range(0, max_val + 1, step)}
            results[f"{t1} n {t2}"] = values
    return results


def compute_complements(memberships: Dict[str, Callable[[float], float]],
                        step: int = 10, max_val: int = 100) -> Dict[str, Dict[int, float]]:
    """Berechnet das Komplement jedes Terms diskretisiert ueber [0, max_val]."""
    results = {}
    for term, func in memberships.items():
        values = {x: round(fuzzy_complement(func(x)), 4) for x in range(0, max_val + 1, step)}
        results[f"nicht({term})"] = values
    return results
