import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
}

df = pd.DataFrame(data)
df["City"] = ["London", "New York", "Tokyo", "Berlin"]


def modify(df_):
# YOUR CODE    return df_


df_modified = modify(df)
print(df_modified)
