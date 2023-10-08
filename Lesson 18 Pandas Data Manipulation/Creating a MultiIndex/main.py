import pandas as pd

# Sample DataFrame
data = {
    "City": ["London", "London", "New York", "New York", "New York", "Tokyo", "Tokyo"],
    "Category": ["Electronics", "Clothing", "Electronics", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Sales": [5000, 3000, 6000, 8000, 4000, 7000, 2000],
}

df = pd.DataFrame(data)

# MultiIndex creation using pd.MultiIndex.from_product()
cities = df['City'].unique()
categories = df['Category'].unique()
index_product = pd.MultiIndex.from_product([cities, categories], names=['City', 'Category'])

# MultiIndex creation using pd.MultiIndex.from_tuples()
index_tuples = df[['City', 'Category']].apply(tuple, axis=1).unique()
index_tuples = pd.MultiIndex.from_tuples(index_tuples, names=['City', 'Category'])

# Creating a multiindex using set_index() method
df = df.set_index(["City", "Category"])
print(df)
print(df.index)
