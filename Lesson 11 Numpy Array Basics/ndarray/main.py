import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

if __name__ == "__main__":
    print(type(a))
    print(a)
    print(f'Array shape: {a.shape}')
    print(f'Number of dimensions: {a.ndim}')
    print(f'Array size: {a.size}')
    print(f'Array data type: {a.dtype}')
