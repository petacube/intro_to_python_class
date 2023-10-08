import numpy as np
import pandas as pd

data = np.array([3, 7, 0, 1, 9])

s = pd.Series(data, index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], name='Number of commits')

if __name__ == "__main__":
    print(s)
    print(s.to_numpy())
