def add_power_balance(QB, dataset, vi, lam=5.0):
    imbalance = (
        dataset["transformer_energy"]
        - sum(dataset["metered_load"].values())
        - dataset["technical_loss"]
    )

    for node in dataset["nodes"]:
        i = vi.var_to_idx[f"theft_{node}"]
        QB.add_linear(i, lam)

    return imbalance
