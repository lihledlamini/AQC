import numpy as np

def load_pseudo_dataset(seed=0):
    np.random.seed(seed)

    nodes = ["C1", "C2", "C3", "C4"]
    edges = [("C1","C2"), ("C2","C3"), ("C3","C4")]

    true_load = {"C1":30, "C2":25, "C3":20, "C4":15}
    theft = {"C3":5, "C4":3}

    metered = {n: true_load[n] - theft.get(n, 0) for n in true_load}

    load_ts = {
        n: np.random.normal(metered[n], 1.0, 24)
        for n in metered
    }

    return {
        "nodes": nodes,
        "edges": edges,
        "true_load": true_load,
        "metered_load": metered,
        "load_timeseries": {0: load_ts},
        "technical_loss": 2.0,
        "transformer_energy": sum(true_load.values()) + 2.0,
        "priors": {"C3":0.7, "C4":0.6}
    }