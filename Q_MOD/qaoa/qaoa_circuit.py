# qaoa/qaoa_circuit.py
import pennylane as qml
from qaoa.mixers import x_mixer, xy_mixer

def build_qaoa(H, p, mixer="X", pairs=None, return_state=False):
    wires = list(H.wires)
    dev = qml.device("default.qubit", wires=wires)

    @qml.qnode(dev)
    def circuit(params):
        gammas = params[:p]
        betas = params[p:]

        # Apply Hadamards on all wires
        for w in wires:
            qml.Hadamard(w)

        # QAOA layers
        for l in range(p):
            qml.templates.ApproxTimeEvolution(H, gammas[l], 1)

            if mixer == "X":
                x_mixer(betas[l], wires)
            else:
                xy_mixer(betas[l], pairs)

        return qml.state() if return_state else qml.expval(H)

    return circuit

