"""
==============================================================================
Module:      membership.py
Description: Mathematical definitions of triangular, trapezoidal, and piecewise
             linear fuzzy membership functions for environmental and behavioral domains.
==============================================================================
"""

import numpy as np
from typing import Dict, Callable


def triangular(x: float, a: float, b: float, c: float) -> float:
    """Berechnet den Zugehoerigkeitsgrad einer Dreiecksfunktion."""
    if b == a or c == b:
        return 1.0 if x == b else 0.0
    return float(max(min((x - a) / (b - a), (c - x) / (c - b)), 0.0))


def trapezoidal(x: float, a: float, b: float, c: float, d: float) -> float:
    """Berechnet den Zugehoerigkeitsgrad einer Trapezfunktion."""
    if b == a or d == c:
        return 1.0 if b <= x <= c else 0.0
    return float(max(min((x - a) / (b - a), 1.0, (d - x) / (d - c)), 0.0))


def get_temperature_memberships() -> Dict[str, Callable[[float], float]]:
    """Gibt linguistische Terme fuer die Umgebungstemperatur [0, 40] Grad Celsius zurueck."""
    return {
        "Sehr niedrig": lambda x: triangular(x, 0, 0, 10),
        "Niedrig": lambda x: trapezoidal(x, 0, 10, 15, 20),
        "Mittel": lambda x: triangular(x, 15, 20, 25),
        "Ueberdurchschnittlich": lambda x: trapezoidal(x, 20, 25, 30, 35),
        "Hoch": lambda x: triangular(x, 30, 35, 40),
        "Sehr hoch": lambda x: triangular(x, 35, 40, 40)
    }


def get_humidity_memberships() -> Dict[str, Callable[[float], float]]:
    """Gibt linguistische Terme fuer die relative Luftfeuchtigkeit [0, 100] Prozent zurueck."""
    return {
        "Sehr gering": lambda x: triangular(x, 0, 0, 20),
        "Gering": lambda x: trapezoidal(x, 10, 20, 30, 40),
        "Mittel": lambda x: triangular(x, 30, 50, 70),
        "Gehoben": lambda x: trapezoidal(x, 60, 70, 80, 90),
        "Hoch": lambda x: triangular(x, 80, 90, 100),
        "Sehr hoch": lambda x: triangular(x, 90, 100, 100),
        "Maximal": lambda x: triangular(x, 95, 100, 100)
    }


class SatisfactionScale:
    """Linguistische Modellierung der Kundenzufriedenheit auf der Skala [0, 10]."""

    @staticmethod
    def very_dissatisfied(x: np.ndarray) -> np.ndarray:
        return np.maximum(1.0 - x / 3.0, 0.0)

    @staticmethod
    def dissatisfied(x: np.ndarray) -> np.ndarray:
        return np.maximum(np.minimum((x - 2.0) / 2.0, (6.0 - x) / 2.0), 0.0)

    @staticmethod
    def neutral(x: np.ndarray) -> np.ndarray:
        return np.maximum(np.minimum(x - 4.0, 6.0 - x), 0.0)

    @staticmethod
    def satisfied(x: np.ndarray) -> np.ndarray:
        return np.maximum(np.minimum((x - 6.0) / 2.0, (9.0 - x) / 2.0), 0.0)

    @staticmethod
    def very_satisfied(x: np.ndarray) -> np.ndarray:
        return np.maximum((x - 7.0) / 3.0, 0.0)
