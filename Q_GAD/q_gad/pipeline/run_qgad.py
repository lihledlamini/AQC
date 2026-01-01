import numpy as np
import pennylane as qml
from collections import Counter

from q_gad.data.pseudo_data import load_pseudo_dataset
from q_gad.graph.edge_weights import compute_multiperiod_edge_weights
from q_gad.variables.variable_index import build_variable_index
from q_gad.qubo.qubo_builder import QUBOBuilder
from q_gad.qubo.qubo_factory import build_qubo
from q_gad.hamiltonian.qubo_to_ising import qubo_to_ising
from q_gad.qaoa.qaoa_circuit import build_qaoa, build_qaoa_sampler


# -----------------------------
# QAOA OPTIMIZATION
# -----------------------------
def optimize_qaoa(qnode, p, steps=60, lr=0.1):
    opt = qml.AdamOptimizer(lr)

    params = (
        np.random.uniform(0, np.pi, p),
        np.random.uniform(0, np.pi, p)
    )

    for step in range(steps):
        params = opt.step(qnode, params)
        if step % 10 == 0:
            print(f"Step {step:02d} | ⟨H⟩ = {qnode(params):.4f}")

    return params


# -----------------------------
# THEFT RISK + CONFIDENCE
# -----------------------------
def compute_theft_risk_with_ci(counts, vi, z=1.96):
    """
    Compute theft probability and 95% confidence interval
    using binomial proportion confidence bounds.
    """
    total = sum(counts.values())
    risk = {}

    for idx, var in vi.idx_to_var.items():
        successes = sum(
            freq for bits, freq in counts.items()
            if bits[idx] == 1
        )

        p = successes / total
        sigma = np.sqrt(p * (1 - p) / total)

        risk[var] = {
            "mean": p,
            "ci_low": max(0.0, p - z * sigma),
            "ci_high": min(1.0, p + z * sigma),
        }

    return risk


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def main():
    print("\n=== Q-GAD: Quantum-Enhanced Graph Anomaly Detection ===\n")

    # 1. Load data
    data = load_pseudo_dataset()

    # 2. Variable indexing
    vi = build_variable_index(data)

    # 3. Edge weights (multi-period MaxCut)
    weights = compute_multiperiod_edge_weights(
        data["load_timeseries"],
        data["edges"]
    )

    # 4. Build QUBO
    QB = QUBOBuilder(vi.size())
    build_qubo(QB, data, vi, data["edges"], weights)

    # 5. QUBO → Ising Hamiltonian
    H = qubo_to_ising(QB.Q)

    # 6. Build QAOA expectation circuit
    qnode = build_qaoa(H, p=2, n_qubits=vi.size())

    # 7. Optimize parameters
    optimal_params = optimize_qaoa(qnode, p=2)

    # 8. Sampling circuit
    sampler = build_qaoa_sampler(H, p=2, n_qubits=vi.size())
    samples = sampler(optimal_params)

    counts = Counter(tuple(s) for s in samples)

    # 9. Theft risk + confidence intervals
    risk = compute_theft_risk_with_ci(counts, vi)

    # 10. Report
    print("\n--- Theft Risk Assessment (with 95% CI) ---")
    for var, stats in sorted(
        risk.items(), key=lambda x: -x[1]["mean"]
    ):
        print(
            f"{var:12s} | "
            f"risk={stats['mean']:.2f} "
            f"[{stats['ci_low']:.2f}, {stats['ci_high']:.2f}]"
        )


if __name__ == "__main__":
    main()
