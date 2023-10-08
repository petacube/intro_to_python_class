import numpy as np
rng = np.random.default_rng()

a = rng.integers(100, size=(5, 20))


b = # Sort columns
ind = # Indices to sort rows
c = # Sort rows using indices ind


if __name__ == '__main__':
    print('\nUnsorted array:\n', a)
    print('\nSorted columns:\n', b)
    print('\nIndices to sort rows:\n', ind)
    print('\nSorted:\n', c)
