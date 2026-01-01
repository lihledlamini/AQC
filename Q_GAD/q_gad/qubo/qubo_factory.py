from .maxcut_terms import add_maxcut_terms
from .physics_terms import add_power_balance
from .priors import add_priors

def build_qubo(QB, dataset, vi, edges, weights):
    add_maxcut_terms(QB, edges, weights, vi)
    add_power_balance(QB, dataset, vi)
    add_priors(QB, dataset.get("priors", {}), vi)
