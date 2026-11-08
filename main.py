"""
==============================================================================
Project:     Fuzzy Logic, Fuzzy Arithmetic & System Reliability Suite
File:        main.py
Author:      Yevhen Biezhyn
Description: Unified CLI orchestrator executing linguistic fuzzy evaluations,
             set operations, Zadeh's extension arithmetic, and system reliability.
==============================================================================
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt

from modules.membership import (
    get_temperature_memberships,
    get_humidity_memberships,
    SatisfactionScale
)
from modules.fuzzy_operations import (
    compute_pairwise_unions,
    compute_pairwise_intersections,
    compute_complements
)
from modules.fuzzy_arithmetic import (
    multiply_triangular_fuzzy_numbers,
    format_fuzzy_number
)
from modules.system_reliability import calculate_hybrid_system_reliability


def print_banner(title: str):
    print("\n" + "=" * 78)
    print(f"  {title.upper()}")
    print("=" * 78)


def run_satisfaction_visualization(save_plot: bool = False):
    print_banner("1. Modul: Linguistische Modellierung der Kundenzufriedenheit")
    x = np.linspace(0, 10, 200)

    vd = SatisfactionScale.very_dissatisfied(x)
    d  = SatisfactionScale.dissatisfied(x)
    n  = SatisfactionScale.neutral(x)
    s  = SatisfactionScale.satisfied(x)
    vs = SatisfactionScale.very_satisfied(x)

    # Operationen berechnen
    op_union = np.maximum(d, n)
    op_inter = np.minimum(s, vs)
    op_neg   = 1.0 - vd

    print("[*] Zufriedenheitsskala [0, 10] mit 5 Termen evaluiert.")
    print("    - Vereinigung: Dissatisfied u Neutral")
    print("    - Schnittmenge: Satisfied n Very Satisfied")
    print("    - Negation: nicht(Very Dissatisfied)")

    plt.figure(figsize=(11, 7))
    plt.plot(x, vd, label="Sehr unzufrieden")
    plt.plot(x, d,  label="Unzufrieden")
    plt.plot(x, n,  label="Neutral")
    plt.plot(x, s,  label="Zufrieden")
    plt.plot(x, vs, label="Sehr zufrieden")

    plt.plot(x, op_union, 'k--', label="Vereinigung (D u N)")
    plt.plot(x, op_inter, 'b:', linewidth=2, label="Schnittmenge (S n VS)")
    plt.plot(x, op_neg,   'r-.', label="Negation (nicht VD)")

    plt.xlabel("Zufriedenheitsgrad")
    plt.ylabel("Zugehoerigkeitsgrad mu(x)")
    plt.title("Linguistische Terme und fundamentale Fuzzy-Operationen")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    if save_plot:
        plt.savefig("fuzzy_satisfaction.png", dpi=300, bbox_inches='tight')
        print("[+] Diagramm gespeichert: fuzzy_satisfaction.png")
        plt.close()
    else:
        plt.show()


def run_environmental_analysis():
    print_banner("2. Modul: Umgebungsklima (Temperatur & Feuchtigkeit)")
    temp_mem = get_temperature_memberships()
    hum_mem = get_humidity_memberships()

    temp_test_points = [5, 15, 25, 35]
    hum_test_points = [10, 30, 60, 90]

    print("[*] Diskrete Auswertung der Temperaturstufen:")
    for t_val in temp_test_points:
        degrees = [f"{term}: {func(t_val):.2f}" for term, func in temp_mem.items() if func(t_val) > 0.0]
        print(f"    - Temperatur {t_val:2d} °C -> {', '.join(degrees)}")

    print("\n[*] Diskrete Auswertung der Luftfeuchtigkeit:")
    for h_val in hum_test_points:
        degrees = [f"{term}: {func(h_val):.2f}" for term, func in hum_mem.items() if func(h_val) > 0.0]
        print(f"    - Feuchtigkeit {h_val:2d} % -> {', '.join(degrees)}")

    # Paarweise Operationen
    unions = compute_pairwise_unions(temp_mem, step=20, max_val=40)
    intersections = compute_pairwise_intersections(temp_mem, step=20, max_val=40)
    complements = compute_complements(temp_mem, step=20, max_val=40)

    sample_pair = list(unions.keys())[0]
    print(f"\n[*] Beispiel-Vereinigung [{sample_pair}] (Auszug):")
    print("   ", unions[sample_pair])


def run_fuzzy_arithmetic_suite():
    print_banner("3. Modul: Fuzzy-Arithmetik (Zadehs Erweiterungsprinzip)")
    a = (2.0, 3.0, 4.0)
    b = (1.0, 2.0, 3.0)
    z = multiply_triangular_fuzzy_numbers(a, b)

    print(f"[*] Faktor A (Dreiecks-Fuzzy-Zahl) : {format_fuzzy_number(a)}")
    print(f"[*] Faktor B (Dreiecks-Fuzzy-Zahl) : {format_fuzzy_number(b)}")
    print(f"[+] Produkt Z = A x B              : {format_fuzzy_number(z)}")
    print(f"    Untere Grenze : {z[0]:.2f}")
    print(f"    Modalwert     : {z[1]:.2f}")
    print(f"    Obere Grenze  : {z[2]:.2f}")


def run_reliability_suite():
    print_banner("4. Modul: Systemzuverlaessigkeit & Redundanzanalyse")
    # P1=0.99, P2=0.98 in Serie; P3=0.95, P4=0.95 parallel redundant
    p_series = [0.99, 0.98]
    p_parallel = [0.95, 0.95]

    p_sys, r_par = calculate_hybrid_system_reliability(p_series, p_parallel)

    print("[*] Komponentenwahrscheinlichkeiten:")
    print("    - Hauptpfad (in Serie)     : P1 = 0.99, P2 = 0.98")
    print("    - Redundanter Block (parallel): P3 = 0.95, P4 = 0.95")
    print(f"[*] Zuverlaessigkeit des redundanten Blocks: {r_par:.6f} (99.75 %)")
    print(f"[+] Gesamtzuverlaessigkeit des Gesamtsystems: {p_sys:.7f} ({p_sys * 100:.4f} %)")


def main():
    parser = argparse.ArgumentParser(
        description="Fuzzy Logic, Fuzzy Arithmetic & Reliability Suite",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--module",
        choices=["all", "satisfaction", "environmental", "arithmetic", "reliability"],
        default="all",
        help=(
            "all           : Fuehrt die gesamte Suite aus (Standard)\n"
            "satisfaction  : Kundenzufriedenheitsskala & Plot\n"
            "environmental : Klima-Zugehoerigkeiten & Mengenoperationen\n"
            "arithmetic    : Multiplikation von Fuzzy-Zahlen (Zadeh)\n"
            "reliability   : Zuverlaessigkeit von Serien-Parallel-Systemen"
        )
    )
    parser.add_argument("--save-plot", action="store_true", help="Speichert das Zufriedenheitsdiagramm als PNG")
    args = parser.parse_args()

    print("=" * 78)
    print("  FUZZY LOGIC, ARITHMETIC & RELIABILITY SUITE")
    print("=" * 78)

    dispatch = {
        "satisfaction": lambda: run_satisfaction_visualization(args.save_plot),
        "environmental": run_environmental_analysis,
        "arithmetic": run_fuzzy_arithmetic_suite,
        "reliability": run_reliability_suite,
    }

    if args.module == "all":
        for fn in dispatch.values():
            fn()
    else:
        dispatch[args.module]()

    print("\n" + "=" * 78)
    print("  BERECHNUNGEN ERFOLGREICH ABGESCHLOSSEN.")
    print("=" * 78 + "\n")


if __name__ == "__main__":
    main()
