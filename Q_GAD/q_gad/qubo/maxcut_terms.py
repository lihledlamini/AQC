def add_maxcut_terms(QB, edges, weights, vi, lam=1.0):
    for (u,v), w in zip(edges, weights):
        i = vi.var_to_idx[f"theft_{u}"]
        j = vi.var_to_idx[f"theft_{v}"]
        QB.add_quadratic(i, j, lam * w)
