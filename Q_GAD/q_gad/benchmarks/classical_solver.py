import numpy as np
import itertools

def qubo_energy(x, Q):
    """
    Compute energy x^T Q x
    """
    return x @ Q @ x


def brute_force_qubo(Q):
    """
    Exact solver for small QUBO problems.

    Parameters
    ----------
    Q : np.ndarray
        QUBO matrix

    Returns
    -------
    best_x : np.ndarray
        Optimal binary solution
    best_energy : float
        Minimum energy
    """
    n = Q.shape[0]
    best_energy = np.inf
    best_x = None

    for bits in itertools.product([0, 1], repeat=n):
        x = np.array(bits)
        E = qubo_energy(x, Q)
        if E < best_energy:
            best_energy = E
            best_x = x.copy()

    return best_x, best_energy


def rank_variables(x, vi):
    """
    Rank anomaly variables by importance.
    """
    anomalies = []
    for idx, val in enumerate(x):
        if val == 1:
            anomalies.append(vi.idx_to_var[idx])
    return anomalies
