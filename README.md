# AQC — Quantum Optimization Pipeline

## Execution Flow

```mermaid
flowchart TD
    A["Start<br/>run_pipeline.py"]
    B["load_dataset()<br/>nodes, edges, demand"]
    C["build_variable_index()<br/>bit → qubit"]
    D["QUBOBuilder()"]
    E["add_linear()<br/>costs & penalties"]
    F["add_quadratic()<br/>constraints"]
    G["Q matrix assembled"]
    H["qubo_to_ising(Q)<br/>Ising Hamiltonian"]
    I["Hamiltonian H(Z)"]
    J["build_qaoa(H, p)"]
    K["QAOA QNode"]
    L["Optimization Loop<br/>γ, β updates"]
    M["Minimum Energy"]
    N["Decode Solution"]
    O["End"]

    A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M --> N --> O
