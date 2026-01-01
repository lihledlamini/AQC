def add_priors(QB, priors, vi, scale=2.0):
    for node, p in priors.items():
        i = vi.var_to_idx[f"theft_{node}"]
        QB.add_linear(i, scale * (1 - p))
