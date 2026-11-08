"""
==============================================================================
Module:      system_reliability.py
Description: Reliability engineering and redundancy modeling for fault-tolerant
             hybrid series-parallel topological system configurations.
==============================================================================
"""

from typing import List, Tuple


def calculate_parallel_reliability(probabilities: List[float]) -> float:
    """
    Berechnet die Zuverlässigkeit eines parallelen (redundanten) Subsystems:
    R_parallel = 1 - PROD(1 - P_i)
    """
    unreliability = 1.0
    for p in probabilities:
        unreliability *= (1.0 - p)
    return float(1.0 - unreliability)


def calculate_hybrid_system_reliability(p_series: List[float], p_parallel: List[float]) -> Tuple[float, float]:
    """
    Berechnet die Gesamtzuverlässigkeit eines Systems, bestehend aus seriellen
    Komponenten und einem parallelen redundanten Block:
    P_s = PROD(P_series) * (1 - PROD(1 - P_parallel))
    """
    r_parallel = calculate_parallel_reliability(p_parallel)
    r_series = 1.0
    for p in p_series:
        r_series *= p

    p_system = float(r_series * r_parallel)
    return p_system, r_parallel
