import numpy as np


def find_most_frequent_class(data_file):
    csv = np.genfromtxt(data_file, delimiter=',', skip_header=1)
    data, labels = csv[:, 1:], np.array(csv[:, 0], dtype=np.int64)

    return # TODO


if __name__ == '__main__':
    most_frequent_class = find_most_frequent_class('data.csv')
    print("Class #", most_frequent_class)
