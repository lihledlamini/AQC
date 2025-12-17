# hamiltonian/qubo_to_ising.py
import pennylane as qml

def qubo_to_ising(Q):
    n = Q.shape[0]
    coeffs, ops = [], []
    const = 0.0


    for i in range(n):
        for j in range(i, n):
            q = Q[i, j]
            if q == 0:
                continue
            if i == j:
                const += q / 2
                coeffs.append(-q / 2)
                ops.append(qml.PauliZ(i))
            else:
                const += q / 4
                coeffs += [-q/4, -q/4, q/4]
                ops += [qml.PauliZ(i), qml.PauliZ(j), qml.PauliZ(i) @ qml.PauliZ(j)]


    if const != 0:
        coeffs.append(const)
        ops.append(qml.Identity(0))


    return qml.Hamiltonian(coeffs, ops)
