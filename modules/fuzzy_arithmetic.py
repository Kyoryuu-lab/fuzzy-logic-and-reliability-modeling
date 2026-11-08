"""
==============================================================================
Module:      fuzzy_arithmetic.py
Description: Fuzzy number arithmetic and Zadeh's extension principle.
             Calculates algebraic product boundaries for triangular fuzzy numbers.
==============================================================================
"""

from typing import Tuple


def multiply_triangular_fuzzy_numbers(a: Tuple[float, float, float],
                                      b: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Multipliziert zwei Dreiecks-Fuzzy-Zahlen A = (a1, a2, a3) und B = (b1, b2, b3)
    nach Zadehs Erweiterungsprinzip: Z = A x B.

    Die unteren und oberen Grenzen werden ueber die Extremwerte der Eckpunktprodukte gebildet:
      z1 = min(a1*b1, a1*b3, a3*b1, a3*b3)
      z2 = a2*b2
      z3 = max(a1*b1, a1*b3, a3*b1, a3*b3)
    """
    a1, a2, a3 = a
    b1, b2, b3 = b

    products = [a1 * b1, a1 * b3, a3 * b1, a3 * b3]
    z1 = min(products)
    z2 = a2 * b2
    z3 = max(products)

    return (float(z1), float(z2), float(z3))


def format_fuzzy_number(num: Tuple[float, float, float]) -> str:
    """Formatiert eine Dreiecks-Fuzzy-Zahl fuer die Konsolenausgabe."""
    return f"({num[0]:.2f}, {num[1]:.2f}, {num[2]:.2f})"
