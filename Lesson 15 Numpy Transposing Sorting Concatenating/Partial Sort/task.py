import numpy as np
rng = np.random.default_rng()

k = 3
mu = 1
sigma = 1
arr = rng.normal(mu, sigma, 20)
target = 0
distances = abs(arr - target)

indices = # TODO
partitioned_by_distance = # TODO
k_nearest = # TODO

if __name__ == '__main__':
    print('Data:\n', arr)
    print('\nDistances from target value:\n', distances)
    print('\nIndices of partitioned data:\n', indices)
    print('\nPartitioned data:\n', partitioned_by_distance)
    print('\nK=3 nearest data points\n', k_nearest)
