#discretization.py
# simple defination for now.
def binary_weights(K, delta):
    return [delta * (2 ** k) for k in range(K)]
