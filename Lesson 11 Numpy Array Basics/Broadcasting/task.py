import numpy as np

rng = np.random.default_rng()

x = np.arange(10)
# TODO: modify x so that the print statement does not throw an exception
y = np.ones(7)

w = rng.integers(2, size=(4, 3))
# TODO: modify w so that the print statement does not throw an exception
z = np.ones((3, 4))

if __name__ == '__main__':
    print(x)
    print(y)
    print(x + y)
    print(z)
    print(w)
    print(z * w)
