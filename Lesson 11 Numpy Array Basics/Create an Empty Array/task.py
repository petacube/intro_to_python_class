import numpy as np


def create_arrays(x, y):
    # TODO
    return a, b


if __name__ == '__main__':
    arrays = create_arrays(3, 4)
    print('\narray of int using ones:')
    print(arrays[0])
    print(f'dtype: {arrays[0].dtype}')
    print('\nTrue Boolean Array using .full:')
    print(arrays[1])
    print(f'dtype: {arrays[1].dtype}')

    print(arrays[0].shape)
