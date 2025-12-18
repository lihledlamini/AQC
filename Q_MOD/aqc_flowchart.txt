from graphviz import Digraph

# Create directed graph
dot = Digraph(
    name="AQC_Flowchart",
    format="svg",
    graph_attr={
        "rankdir": "TB",
        "fontsize": "10",
        "fontname": "Helvetica"
    },
    node_attr={
        "shape": "box",
        "style": "rounded",
        "fontname": "Helvetica"
    }
)

# Nodes
dot.node(
    "A",
    "Pseudo / Real Dataset\n(nodes, edges, loads)"
)

dot.node(
    "B",
    "Discretization Layer\n(continuous → binary)\nencoding / discretization"
)

dot.node(
    "C",
    "Variable Indexing\n(bit → qubit mapping)\nqubo / variable_index"
)

dot.node(
    "D",
    "QUBO Construction\nObjective + Penalties\nqubo / qubo_builder"
)

dot.node(
    "E",
    "QUBO → Ising Mapping\nHamiltonian H(Z)\nhamiltonian / ising"
)

dot.node(
    "F",
    "QAOA Circuit Builder\nProblem + Mixer Layers\nqaoa / qaoa_circuit"
)

dot.node(
    "G",
    "Quantum Backend\n(Simulator / Hardware)"
)

dot.node(
    "H",
    "Measurement & Analysis\nEnergy, bitstrings"
)

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")
dot.edge("G", "H")

# Render
dot.render("aqc_flowchart", cleanup=True)

