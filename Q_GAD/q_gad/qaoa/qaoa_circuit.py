import pennylane as qml
import numpy as np

def build_qaoa(H, p, n_qubits):
    dev = qml.device("lightning.kokkos", wires=n_qubits)

    @qml.qnode(dev)
    def circuit(params):
        gammas, betas = params
        for i in range(n_qubits):
            qml.Hadamard(i)
        for k in range(p):
            qml.ApproxTimeEvolution(H, gammas[k], 1)
            for i in range(n_qubits):
                qml.RX(2 * betas[k], i)
        return qml.expval(H)

    return circuit
def build_qaoa_sampler(H, p, n_qubits):
    dev = qml.device("lightning.kokkos", wires=n_qubits, shots=1000)

    @qml.qnode(dev)
    def sampler(params):
        gammas, betas = params

        for i in range(n_qubits):
            qml.Hadamard(i)

        for k in range(p):
            qml.ApproxTimeEvolution(H, gammas[k], 1)
            for i in range(n_qubits):
                qml.RX(2 * betas[k], i)

        return qml.sample()

    return sampler
