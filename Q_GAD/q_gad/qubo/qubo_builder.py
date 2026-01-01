import numpy as np

class QUBOBuilder:
    def __init__(self, n):
        self.Q = np.zeros((n,n))

    def add_linear(self, i, c):
        self.Q[i,i] += c

    def add_quadratic(self, i, j, c):
        self.Q[i,j] += c
        self.Q[j,i] += c
