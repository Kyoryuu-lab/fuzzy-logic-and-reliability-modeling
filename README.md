<h1>fuzzy-logic-and-reliability-modeling</h1>
<p>Computational Soft Computing suite in Python: fuzzy membership modeling, set operations, triangular fuzzy arithmetic (Zadeh's extension principle), and engineering system reliability</p>

<h2>Project description</h2>
<p>This repository provides a modular, production-grade computational framework covering fundamental methods in fuzzy set theory, approximate reasoning, and fault-tolerant reliability analysis:</p>
<ol>
  <li>
    <dl>
      <dt><b>Linguistic Variable &amp; Membership Functions:</b></dt>
      <dd>Implements analytical triangular ($\Lambda$) and trapezoidal ($\Pi$) membership functions with bounded edge-case handling.</dd>
      <dd>Models physical domains for climate control (ambient temperature $[0, 40]^\circ\text{C}$ and relative humidity $[0, 100]\%$) alongside a 5-term satisfaction scale $[0, 10]$.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Fuzzy Set Operations (Norms &amp; Conorms):</b></dt>
      <dd><b>Fuzzy Union (S-Norm):</b> Disjunctive aggregation $\mu_{A \cup B}(x) = \max(\mu_A(x), \mu_B(x))$.</dd>
      <dd><b>Fuzzy Intersection (T-Norm):</b> Conjunctive aggregation $\mu_{A \cap B}(x) = \min(\mu_A(x), \mu_B(x))$.</dd>
      <dd><b>Fuzzy Complement (Negation):</b> Involutive inversion $\mu_{\neg A}(x) = 1 - \mu_A(x)$.</dd>
      <dd>Generates pairwise cross-term relationship matrices across the continuous domain.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Fuzzy Arithmetic via Zadeh's Extension Principle:</b></dt>
      <dd>Calculates algebraic products of triangular fuzzy numbers $A = (a_1, a_2, a_3)$ and $B = (b_1, b_2, b_3)$.</dd>
      <dd>Evaluates support interval bounds via combinatorial endpoint min/max comparisons.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Fault-Tolerant System Reliability:</b></dt>
      <dd>Computes analytical survival probabilities for hybrid series-parallel network topologies.</dd>
      <dd>Quantifies reliability gains achieved through parallel active redundancy: $P_s = P_1 \cdot P_2 \cdot [1 - (1 - P_3)(1 - P_4)]$.</dd>
    </dl>
  </li>
</ol>

<h2>Project files</h2>
<table>
  <tr>
    <th colspan="2">fuzzy-logic-and-reliability-modeling</th>
  </tr>
  <tr>
    <td>main.py</td>
    <td>Master CLI orchestrator running the full analytical suite or targeted modules</td>
  </tr>
  <tr>
    <td>modules/membership.py</td>
    <td>Triangular, trapezoidal, and piecewise satisfaction membership models</td>
  </tr>
  <tr>
    <td>modules/fuzzy_operations.py</td>
    <td>T-norm, T-conorm, negation operators, and pairwise matrix generators</td>
  </tr>
  <tr>
    <td>modules/fuzzy_arithmetic.py</td>
    <td>Triangular fuzzy number multiplication engine based on Zadeh's extension principle</td>
  </tr>
  <tr>
    <td>modules/system_reliability.py</td>
    <td>Reliability engineering formulas for hybrid redundant topological systems</td>
  </tr>
  <tr>
    <td>README.md</td>
    <td>Mathematical documentation and operational guide</td>
  </tr>
  <tr>
    <td>.gitignore</td>
    <td>Exclusion rules for Python bytecode, virtual environments, and generated plots</td>
  </tr>
</table>

<h2>Mathematical Formulation</h2>
<table>
  <tr>
    <th>Domain</th>
    <th>Method</th>
    <th>Analytical Expression</th>
  </tr>
  <tr>
    <td><b>Membership</b></td>
    <td>Triangular Function</td>
    <td>$\mu(x; a, b, c) = \max\left(\min\left(\frac{x-a}{b-a}, \frac{c-x}{c-b}\right), 0\right)$</td>
  </tr>
  <tr>
    <td><b>Membership</b></td>
    <td>Trapezoidal Function</td>
    <td>$\mu(x; a, b, c, d) = \max\left(\min\left(\frac{x-a}{b-a}, 1, \frac{d-x}{d-c}\right), 0\right)$</td>
  </tr>
  <tr>
    <td><b>Fuzzy Arithmetic</b></td>
    <td>Fuzzy Multiplication</td>
    <td>$Z = A \otimes B = (\min_{i,j} a_i b_j, \; a_2 b_2, \; \max_{i,j} a_i b_j) \quad \text{for } i,j \in \{1, 3\}$</td>
  </tr>
  <tr>
    <td><b>Reliability</b></td>
    <td>Hybrid System</td>
    <td>$P_s = P_1 \cdot P_2 \cdot \left[1 - (1 - P_3)(1 - P_4)\right]$</td>
  </tr>
</table>

<h2>Installation and launch</h2>
<ol>
  <b>
    <li>
      <dl>
        <dt>Clone repository</dt>
        <dd>
          <code>git clone https://github.com/Kyoryuu-lab/fuzzy-logic-and-reliability-modeling.git</code>
        </dd>
        <dd>
          <code>cd fuzzy-logic-and-reliability-modeling</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Install dependencies</dt>
        <dd>
          <code>pip install numpy matplotlib</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Run complete analytical suite</dt>
        <dd>
          <code>python main.py --module all --save-plot</code>
        </dd>
        <dd>Execute individual modules: <code>python main.py --module arithmetic</code> (Options: <code>satisfaction</code>, <code>environmental</code>, <code>arithmetic</code>, <code>reliability</code>)</dd>
      </dl>
    </li>
  </b>
</ol>

<h2>Example of console output (python main.py --module all)</h2>
<samp>
  <p>
    ==============================================================================<br />
    &nbsp;&nbsp;1. MODUL: LINGUISTISCHE MODELLIERUNG DER KUNDENZUFRIEDENHEIT<br />
    ==============================================================================<br />
    [*] Zufriedenheitsskala [0, 10] mit 5 Termen evaluiert.<br />
    <br />
    ==============================================================================<br />
    &nbsp;&nbsp;2. MODUL: UMGEBUNGSKLIMA (TEMPERATUR &amp; FEUCHTIGKEIT)<br />
    ==============================================================================<br />
    [*] Diskrete Auswertung der Temperaturstufen:<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Temperatur&nbsp;&nbsp;5 °C -&gt; Sehr niedrig: 0.50, Niedrig: 0.50<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Temperatur 15 °C -&gt; Niedrig: 1.00, Mittel: 0.00<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Temperatur 25 °C -&gt; Mittel: 0.00, Ueberdurchschnittlich: 1.00<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Temperatur 35 °C -&gt; Ueberdurchschnittlich: 0.00, Hoch: 1.00, Sehr hoch: 0.00<br />
    <br />
    ==============================================================================<br />
    &nbsp;&nbsp;3. MODUL: FUZZY-ARITHMETIK (ZADEHS ERWEITERUNGSPRINZIP)<br />
    ==============================================================================<br />
    [*] Faktor A (Dreiecks-Fuzzy-Zahl) : (2.00, 3.00, 4.00)<br />
    [*] Faktor B (Dreiecks-Fuzzy-Zahl) : (1.00, 2.00, 3.00)<br />
    [+] Produkt Z = A x B&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: (2.00, 6.00, 12.00)<br />
    &nbsp;&nbsp;&nbsp;&nbsp;Untere Grenze : 2.00<br />
    &nbsp;&nbsp;&nbsp;&nbsp;Modalwert&nbsp;&nbsp;&nbsp;&nbsp; : 6.00<br />
    &nbsp;&nbsp;&nbsp;&nbsp;Obere Grenze&nbsp;&nbsp;: 12.00<br />
    <br />
    ==============================================================================<br />
    &nbsp;&nbsp;4. MODUL: SYSTEMZUVERLAESSIGKEIT &amp; REDUNDANZANALYSE<br />
    ==============================================================================<br />
    [*] Komponentenwahrscheinlichkeiten:<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Hauptpfad (in Serie)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: P1 = 0.99, P2 = 0.98<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Redundanter Block (parallel): P3 = 0.95, P4 = 0.95<br />
    [*] Zuverlaessigkeit des redundanten Blocks: 0.997500 (99.75 %)<br />
    [+] Gesamtzuverlaessigkeit des Gesamtsystems: 0.9677745 (96.7775 %)<br />
    <br />
    ==============================================================================<br />
    &nbsp;&nbsp;BERECHNUNGEN ERFOLGREICH ABGESCHLOSSEN.<br />
    ==============================================================================
  </p>
