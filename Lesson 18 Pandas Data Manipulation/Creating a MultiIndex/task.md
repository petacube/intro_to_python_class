# Creating a MultiIndex
A [MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html) (or hierarchical index) is an advanced indexing method in pandas that allows you to store and manipulate data with an arbitrary number of dimensions in lower-dimensional data structures like Series and DataFrames.
One of example is using a second index column as a supplement for the first one to identify each row uniquely.

```python
import pandas as pd

# Sample DataFrame
data = {
    "City": ["London", "London", "New York", "New York", "New York", "Tokyo", "Tokyo"],
    "Category": ["Electronics", "Clothing", "Electronics", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Sales": [5000, 3000, 6000, 8000, 4000, 7000, 2000],
}

# Creating a multiindex using set_index() method
df = pd.DataFrame(data).set_index(["City", "Category"]) 
print(df)
```
Output:
```
                      Sales
City     Category          
London   Electronics   5000
         Clothing      3000
New York Electronics   6000
         Electronics   8000
         Clothing      4000
Tokyo    Electronics   7000
         Clothing      2000
```
 You can think of `MultiIndex` as an array of tuples where each tuple is unique. A `MultiIndex` can be created also from a list of arrays (using `pd.MultiIndex.from_arrays()`) or an array of tuples (using `from_tuples()`). When you want every pairing of the elements in two iterables, you should use `pd.MultiIndex.from_product()` method:
```python
# MultiIndex creation using pd.MultiIndex.from_product()
cities = df['City'].unique()
categories = df['Category'].unique()
index_product = pd.MultiIndex.from_product([cities, categories], names=['City', 'Category'])

# MultiIndex creation using pd.MultiIndex.from_tuples()
index_tuples = df[['City', 'Category']].apply(tuple, axis=1).unique()
index_tuples = pd.MultiIndex.from_tuples(index_tuples, names=['City', 'Category'])
```
The initial point to observe regarding `MultiIndex` is that it doesn't actually group elements as one might assume. Internally, it simply consists of a flat series of labels.
```python
print(df.index)
```
Output:
```
MultiIndex([(  'London', 'Electronics'),
            (  'London',    'Clothing'),
            ('New York', 'Electronics'),
            ('New York', 'Electronics'),
            ('New York',    'Clothing'),
            (   'Tokyo', 'Electronics'),
            (   'Tokyo',    'Clothing')],
           names=['City', 'Category'])
```

