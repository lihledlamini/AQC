# qaoa/qaoa_circuit.py
import pennylane as qml
from qaoa.mixers import x_mixer, xy_mixer

def build_qaoa(H, p, mixer="X", pairs=None):
    n = len(H.wires)+10
    dev = qml.device("default.qubit", wires=n)

    @qml.qnode(dev)
    def circuit(params):
        gammas = params[:p]
        betas = params[p:]

        for w in range(n):
            qml.Hadamard(w)

        for l in range(p):
            qml.templates.ApproxTimeEvolution(H, gammas[l], 1)
            if mixer == "X":
                x_mixer(betas[l], range(n))
            else:
                xy_mixer(betas[l], pairs)


        return qml.expval(H)


    return circuit
