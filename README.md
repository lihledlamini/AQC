flowchart TD

    A["Pseudo / Real Dataset<br/>(nodes, edges, loads)"]
    B["Discretization Layer<br/>(continuous → binary)<br/>encoding / discretization"]
    C["Variable Indexing<br/>(bit → qubit mapping)<br/>qubo / variable_index"]
    D["QUBO Construction<br/>Objective + Penalties<br/>qubo / qubo_builder"]
    E["QUBO → Ising Mapping<br/>Hamiltonian H(Z)<br/>hamiltonian / ising"]
    F["QAOA Circuit Builder<br/>Problem + Mixer Layers<br/>qaoa / qaoa_circuit"]
    G["Quantum Backend<br/>(Simulator / Hardware)"]
    H["Measurement & Analysis<br/>Energy, bitstrings"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
