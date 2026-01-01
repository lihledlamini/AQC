import pennylane as qml

def qubo_to_ising(Q):
    coeffs, ops = [], []
    n = Q.shape[0]

    for i in range(n):
        for j in range(i, n):
            q = Q[i,j]
            if q == 0:
                continue
            if i == j:
                coeffs.append(-q/2)
                ops.append(qml.PauliZ(i))
            else:
                coeffs.append(q/4)
                ops.append(qml.PauliZ(i) @ qml.PauliZ(j))

    return qml.Hamiltonian(coeffs, ops)
