# Q-GAD  
## Quantum-Enhanced Graph Anomaly Detection

---

## 1. Overview

**Q-GAD (Quantum-Enhanced Graph Anomaly Detection)** is a hybrid classical–quantum framework for detecting persistent anomalies in networked systems using:

- Graph inconsistency detection (MaxCut)
- Physics-aware constraints (QUBO formulation)
- Quantum Approximate Optimization Algorithm (QAOA)
- Probabilistic risk scoring with confidence intervals

### Primary Use Case
Electricity theft (non-technical losses) in power grids.

### Other Applicable Domains
- Water distribution networks  
- Telecom fraud detection  
- Traffic flow anomalies  
- Supply-chain inconsistencies  

---

## 2. Core Idea

Q-GAD answers the question:

> *Which nodes must be anomalous in order to best explain observed inconsistencies in the network, while respecting physical laws and prior knowledge?*

This is formulated as a **constrained combinatorial optimization problem**, mapped to an **Ising Hamiltonian**, and solved using **quantum optimization**.

---

## 3. Mathematical Formulation (High-Level)

The objective Hamiltonian is:

$$
H = \lambda_1 H_{\text{Graph}} + \lambda_2 H_{\text{Physics}} + \lambda_3 H_{\text{Priors}}
$$

Where:

- **Graph term (MaxCut)**  
  Penalizes inconsistent edges between nodes.

- **Physics term**  
  Enforces conservation laws (e.g., power balance).

- **Prior term**  
  Encodes historical or expert knowledge.

The output is **probabilistic**, not deterministic.

---

## 4. Logical Project Structure (Conceptual)

```text
Q_GAD/
└── q_gad/
    ├── data/           # datasets
    ├── graph/          # edge weighting
    ├── variables/      # binary variable indexing
    ├── qubo/           # optimization formulation
    ├── hamiltonian/    # QUBO → Ising
    ├── qaoa/           # quantum circuits
    ├── benchmarks/     # classical solvers
    └── pipeline/       # end-to-end execution

```    
## 5. End-to-End Code Flow
1. Load network data (nodes, edges, time series)
2. Compute multi-period inconsistency weights
3. Define binary anomaly variables
4. Assemble the QUBO formulation:
   - MaxCut graph terms
   - Physics-based constraints
   - Prior penalty terms
5. Convert the QUBO into an Ising Hamiltonian
6. Optimize the Hamiltonian using QAOA
7. Sample low-energy bitstrings from the quantum circuit
8. Map sampled bitstrings back to network nodes
9. Compute anomaly risk scores with confidence intervals
---
## 6. Pipeline Flowchart
```text
Start (run_qgad)
        |
        v
Load pseudo dataset
        |
        v
Compute multi-period edge weights
        |
        v
Build binary variable index
        |
        v
Assemble QUBO
  - MaxCut
  - Physics constraints
  - Priors
        |
        v
QUBO → Ising Hamiltonian
        |
        v
QAOA optimization (⟨H⟩ minimization)
        |
        v
Sample bitstrings
        |
        v
Risk estimation + confidence intervals
        |
        v
Ranked anomaly report
```
