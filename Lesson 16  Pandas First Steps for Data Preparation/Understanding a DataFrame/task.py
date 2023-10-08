import numpy as np
import pandas as pd

students = ["Alice", "Bob"]
data = np.array([[3, 4], [None, 5], [0, 2], [1, None], [9, 6]])

df = pd.DataFrame(data, index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], columns=students)

if __name__ == "__main__":
    print(df)
