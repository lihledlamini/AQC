# qaoa/mixers.py
import pennylane as qml

def x_mixer(beta, wires):
    for w in wires:
        qml.RX(2 * beta, wires=w)

def xy_mixer(beta, pairs):
    for i, j in pairs:
        qml.IsingXX(2 * beta, wires=[i, j])
        qml.IsingYY(2 * beta, wires=[i, j])
