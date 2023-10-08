import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])

if __name__ == '__main__':
    print(df.loc[['row1', 'row3'], ['A', 'C']])
    print(df.iloc[[0, 2], [0, 2]])
