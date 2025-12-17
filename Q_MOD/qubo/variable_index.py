# qubo/variable_index.py


def build_variable_index(nodes, edges, bits_per_var):
    index = {}
    reverse = {}
    counter = 0


    for i in nodes:
        for var in ['g', 's', 'u', 'x']:
            K = bits_per_var.get((var, i), 1)
            for k in range(K):
                index[(var, i, k)] = counter
                reverse[counter] = (var, i, k)
                counter += 1


    for (i, j) in edges:
        K = bits_per_var.get(('f', i, j), 1)
        for k in range(K):
            index[("f", (i,j), k)] = counter
            reverse[counter] = ("f", (i,j), k)
            counter += 1


    return index, reverse, counter
