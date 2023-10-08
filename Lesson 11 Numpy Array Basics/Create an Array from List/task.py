import numpy as np


def create_array(x, y):
    list_ = [[i for i in range(y)] for i in range(x)]  # We use `list_` instead of
    # `list` here so that the variable name does not shadow the built-in name 'list'
    array_ = # TODO
    return array_


if __name__ == "__main__":
    array = create_array(3, 5)
    print(array)
    print(array.shape)
