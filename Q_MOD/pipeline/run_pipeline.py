# pipeline/run_pipeline.py
import numpy as np
from data.pseudo_data import load_pseudo_dataset
from qubo.variable_index import build_variable_index
from qubo.qubo_builder import QUBOBuilder
from hamiltonian.qubo_to_ising import qubo_to_ising
from qaoa.qaoa_circuit import build_qaoa


# Load data
data = load_pseudo_dataset()
nodes, edges = data["nodes"], data["edges"]


bits = {('g',3):3, ('u',3):2}
index, rev, n = build_variable_index(nodes, edges, bits)


# Example minimal QUBO
Q = QUBOBuilder(n)
Q.add_linear(index[('g',3,0)], 1.8)
Q.add_linear(index[('u',3,0)], -25 * data['L'][3])


Qmat = Q.matrix()


# Hamiltonian
H = qubo_to_ising(Qmat)


# QAOA
qnode = build_qaoa(H, p=1)
params = np.random.rand(2)
print("Energy:", qnode(params))
