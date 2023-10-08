import pandas as pd

data = {
    "City": ["London", "London", "New York", "New York", "New York", "Tokyo", "Tokyo"],
    "Category": ["Electronics", "Clothing", "Electronics", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Sales, 2021": [5000, 3000, 6000, 8000, 4000, 7000, 2000],
    "Sales, 2022": [7000, 2000, 7000, 4000, 5000, 5000, 1000],
    "Offers, 2021": [50, 40, 70, 20, 30, 60, 80],
    "Offers, 2022": [70, 20, 10, 70, 40, 50, 50],
}

df = pd.DataFrame(data).set_index(["City", "Category"])

mi = pd.MultiIndex.from_tuples(
    [("Sales", 2021), ("Sales", 2022), ("Offers", 2021), ("Offers", 2022)],
    names=["Transaction", "Year"]
)
df.columns = mi


def select_2022_columns(df):
# YOUR CODE