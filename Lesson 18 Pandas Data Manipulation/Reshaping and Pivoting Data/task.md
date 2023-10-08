# Reshaping and Pivoting Data
## Melting data (unpivot from wide to long format)
```python
import pandas as pd

# Sample DataFrame (wide format)
data = {
    "ID": [1, 2, 3],
    "Temperature": [23, 21, 25],
    "Humidity": [45, 50, 40],
}

df = pd.DataFrame(data)

print("Original DataFrame (wide format):")
print(df)
```
Output:
```
Original DataFrame (wide format):
   ID  Temperature  Humidity
0   1           23        45
1   2           21        50
2   3           25        40
```

```python
# Melting the DataFrame to long format
melted_df = pd.melt(
    df, id_vars="ID", value_vars=["Temperature", "Humidity"], var_name="Variable", value_name="Value"
)

print("\nMelted DataFrame (long format):")
print(melted_df)
```
Output:
```
Melted DataFrame (long format):
   ID     Variable  Value
0   1  Temperature     23
1   2  Temperature     21
2   3  Temperature     25
3   1     Humidity     45
4   2     Humidity     50
5   3     Humidity     40
```

In this example, the original DataFrame (in wide format) is melted using the [pd.melt()](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) method. The `id_vars` parameter is set to `"ID"`, the `value_vars` parameter is set to `["Temperature", "Humidity"]`, and the `var_name` and `value_name` parameters are set to `"Variable"` and `"Value"`, respectively.

## Pivoting data (long to wide format)
```python
import pandas as pd

# Sample DataFrame (long format)
data = {
    "ID": [1, 2, 3, 1, 2, 3],
    "Variable": ["Temperature", "Temperature", "Temperature", "Humidity", "Humidity", "Humidity"],
    "Value": [23, 21, 25, 45, 50, 40],
}

df = pd.DataFrame(data)

print("Original DataFrame (long format):")
print(df)

# Pivoting the DataFrame to wide format
pivoted_df = df.pivot(index="ID", columns="Variable", values="Value")

print("\nPivoted DataFrame (wide format):")
print(pivoted_df)
```
In the second example, the original DataFrame (in long format) is pivoted using the [pd.pivot()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html) method, which essentially reverses the `pd.melt()` method. The index parameter is set to `"ID"`, the columns parameter is set to `"Variable"`, and the values parameter is set to `"Value"`.


## Pivoting Data with Aggregation

1. Pivot tables
   
    While `pivot()` provides general purpose pivoting with various data types (strings, numerics, etc.), `pandas` also provides `pivot_table()` for pivoting with aggregation of numeric data.
    
    ```python
    import pandas as pd

    # Sample DataFrame
    data = {
        "City": ["London", "London", "New York", "New York", "New York", "Tokyo", "Tokyo"],
        "Category": ["Electronics", "Clothing", "Electronics", "Electronics", "Clothing", "Electronics", "Clothing"],
        "Sales": [5000, 3000, 6000, 8000, 4000, 7000, 2000],
    }
    
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    # Creating a pivot table
    pivot_table = pd.pivot_table(
        df, index="City", columns="Category", values="Sales", aggfunc="sum"
    )
    
    print("\nPivot Table:")
    print(pivot_table)
    ```
    Output:
    ```
    Original DataFrame:
           City     Category  Sales
    0    London  Electronics   5000
    1    London     Clothing   3000
    2  New York  Electronics   6000
    3  New York  Electronics   8000
    4  New York     Clothing   4000
    5     Tokyo  Electronics   7000
    6     Tokyo     Clothing   2000
    Pivot Table:
    Category  Clothing  Electronics
    City                           
    London        3000         5000
    New York      4000        14000
    Tokyo         2000         7000
    ```

    In this example, a pivot table is created using the `pd.pivot_table()` method. The `index` parameter is set to `"City"`, the `columns` parameter is set to `"Category"`, the `values` parameter is set to `"Sales"`, and the `aggfunc` parameter is set to `"sum"` for aggregating the data.

2. Cross-tabulation

    Use [pd.crosstab()](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html#pandas.crosstab) to compute a cross-tabulation of two (or more) factors. By default `crosstab()` computes a frequency table of the factors unless an array of values and an aggregation function are passed.
    ```python
    import pandas as pd
    
    # Sample DataFrame
    data = {
        "Gender": ["M", "M", "F", "F", "M", "F", "M"],
        "AgeGroup": ["18-30", "18-30", "18-30", "31-50", "31-50", "31-50", "18-30"],
        "Purchased": [1, 0, 1, 1, 0, 1, 1],
    }
    
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    # Creating a cross-tabulation
    cross_tab = pd.crosstab(index=df["Gender"], columns=df["AgeGroup"], values=df["Purchased"], aggfunc="sum")
    
    print("\nCross-tabulation:")
    print(cross_tab)
    ```
    Output:
    ```
    Original DataFrame:
      Gender AgeGroup  Purchased
    0      M    18-30          1
    1      M    18-30          0
    2      F    18-30          1
    3      F    31-50          1
    4      M    31-50          0
    5      F    31-50          1
    6      M    18-30          1
    Cross-tabulation:
    AgeGroup  18-30  31-50
    Gender                
    F             1      2
    M             2      0
    ```
