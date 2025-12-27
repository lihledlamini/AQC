# pipeline/run_pipeline.py
import numpy as np
import pennylane as qml
from data.pseudo_data import load_pseudo_dataset
from qubo.variable_index import build_variable_index
from qubo.qubo_builder import QUBOBuilder
from hamiltonian.qubo_to_ising import qubo_to_ising
from qaoa.qaoa_circuit import build_qaoa

def build_qubo(index, dataset, bits):
    Q = QUBOBuilder(len(index))

    W_balance = 10.0  # MUST be positive

    for node in dataset["nodes"]:
        L = dataset["L"].get(node, 0)

        # ---- Generation cost ----
        for k in range(bits.get(('g', node), 1)):
            Q.add_linear(
                index[('g', node, k)],
                dataset["c_gen"].get(node, 0)
            )

        # ---- Renewable incentive ----
        for k in range(bits.get(('u', node), 1)):
            Q.add_linear(
                index[('u', node, k)],
                -dataset["renewables"].get(node, 0)
            )

        # ---- Power balance penalty ----
        if L > 0:
            g_bits = [index[('g', node, k)]
                      for k in range(bits.get(('g', node), 1))]
            u_bits = [index[('u', node, k)]
                      for k in range(bits.get(('u', node), 1))]

            all_bits = g_bits + u_bits

            # Linear terms: +W x_i - 2W L x_i
            for i in all_bits:
                Q.add_linear(i, W_balance)          # x_i^2 term
                Q.add_linear(i, -2 * W_balance * L)

            # Quadratic coupling: +2W x_i x_j
            for i in range(len(all_bits)):
                for j in range(i + 1, len(all_bits)):
                    Q.add_quadratic(
                        all_bits[i],
                        all_bits[j],
                        2 * W_balance
                    )

    return Q.matrix()


# Load data
dataset = load_pseudo_dataset()
nodes, edges = dataset["nodes"], dataset["edges"]

bits = {('g',3):3, ('u',3):2}
index, rev, n = build_variable_index(nodes, edges, bits)
Qmat = build_qubo(index, dataset, bits)

# Hamiltonian
H = qubo_to_ising(Qmat)
# QAOA
qnode_action = build_qaoa(H, p=1)
#params = np.random.rand(2**np.pi, size=2)# initial weights database
## Lets Optimize####
opt = qml.AdamOptimizer(stepsize=0.1)
params = qml.numpy.array(np.random.uniform(0, 2*np.pi, size=2),requires_grad=True)
nlearn = 100
for _ in range(nlearn):
    params=opt.step(qnode_action,params)
    
energy = qnode_action(params)###<------------------

qnode_state=build_qaoa(H,p=1, return_state=True)
state=qnode_state(params)######<--------------------
print("Energy:", qnode_action(params))


probs = np.abs(state)**2
idx = np.argmax(probs)
bitstring = format(idx, f"0{len(H.wires)}b")
print("Lowest-energy state:", bitstring)
print("Probability:", probs[idx])

################### Classical, future test sand box
print ('Running Classical :----------------------')
Hmat = qml.matrix(H)
eigvals, eigvecs = np.linalg.eigh(Hmat)
print("Exact ground energy:", eigvals[0])
fidelity = np.abs(np.vdot(eigvecs[:, 0], state))**2
print("Fidelity:", fidelity)

################## Mapping back to database############
def map_bitstring_to_dataset(bitstring, rev):
    mapping = {}
    n = len(bitstring)
    for i in range(n):
        mapping[rev[i]] = int(bitstring[i])
    return mapping

# --- Extract dominant bitstring from QAOA state ---
bitstring_index = np.argmax(np.abs(state)**2)
bitstring = format(bitstring_index, f"0{len(rev)}b")  # ensure bitstring length = number of qubits

# --- Map qubits back to dataset variables ---
solution_mapping = map_bitstring_to_dataset(bitstring, rev)

# --- Summarize per node ---
dataset = load_pseudo_dataset()
node_summary = {}
for (typ, node, idx), val in solution_mapping.items():
    if typ in ['g', 'u']:  # only generator or renewable
        if node not in node_summary:
            node_summary[node] = {}
        node_summary[node][typ] = val

# --- Print summary with costs ---
for node, info in node_summary.items():
    gen_cost = dataset["c_gen"].get(node, 0) * info.get("g",0)
    renewable = dataset["renewables"].get(node,0) * info.get("u",0)
    print(f"Node {node}: Generation ON={info.get('g',0)}, Renewable ON={info.get('u',0)}, Cost={gen_cost}, Renewable output={renewable}")




