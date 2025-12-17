# qubo/qubo_builder.py
import numpy as np
from encoding.discretization import binary_weights


class QUBOBuilder:
def __init__(self, n):
self.Q = np.zeros((n, n))


def add_linear(self, i, v):
self.Q[i, i] += v


def add_quadratic(self, i, j, v):
a, b = min(i, j), max(i, j)
self.Q[a, b] += v


def matrix(self):
return self.Q
