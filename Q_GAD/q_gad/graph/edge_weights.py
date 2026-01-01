import numpy as np

def compute_multiperiod_edge_weights(load_ts_by_period, edges, alpha=1.0, beta=1.0):
    weights = {e:0.0 for e in edges}

    for period in load_ts_by_period:
        ts = load_ts_by_period[period]
        for i, j in edges:
            Li, Lj = ts[i], ts[j]
            mean_diff = abs(Li.mean() - Lj.mean())
            corr = np.corrcoef(Li, Lj)[0,1]
            weights[(i,j)] += alpha * mean_diff + beta * (1 - corr)

    return [weights[e] for e in edges]
