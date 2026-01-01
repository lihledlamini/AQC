class VariableIndex:
    def __init__(self):
        self.var_to_idx = {}
        self.idx_to_var = {}
        self._n = 0

    def add(self, name):
        self.var_to_idx[name] = self._n
        self.idx_to_var[self._n] = name
        self._n += 1

    def size(self):
        return self._n


def build_variable_index(dataset):
    vi = VariableIndex()
    for node in dataset["nodes"]:
        vi.add(f"theft_{node}")
    return vi
