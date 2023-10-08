## groupby()
A frequent operation in data processing involves computing statistics for specific groups within the data rather than the entire dataset. The initial step is to create a lazy object by defining the criteria for dividing a Series (or a DataFrame) into distinct groups. This lazy object doesn't have a meaningful representation on its own, but it can be:
* iterable, i.e. to yield the grouping key and the corresponding sub-series (great for debugging)
    ```python
    import pandas as pd
    
    students = pd.Series(["Alice", "Bob", "Charlie", "David"])
    name_lengths = students.str.len()
    for key, value in students.groupby(name_lengths):
        print(f"key = {key}, value.values = {value.values}")
    ```
    Output:
    ```
    key = 3, value.values = ['Bob']
    key = 5, value.values = ['Alice' 'David']
    key = 7, value.values = ['Charlie']
    ```
* accessed in the same way as regular Series to obtain a specific property of each group (which is faster than using iteration):
    ```python
    import pandas as pd
  
    numbers = pd.Series([1, 3, 7, 9, 17, 23, 29])
    last_digits_gb = numbers.groupby(numbers % 10)
  
    print(numbers.values)
    print(f"By last digit: \ncount = \n{last_digits_gb.count()}\nsum = \n{last_digits_gb.sum()}")
    ```
    Output:
    ```
    [ 1  3  7  9 17 23 29]
    By last digit: 
    count = 
    1    1
    3    2
    7    2
    9    2
    dtype: int64
    sum = 
    1     1
    3    26
    7    24
    9    38
    dtype: int64
    ```
In this example, we divide the series into four groups based on the last digit of number (remainder of dividing the values by 10). For each group, we obtain number of elements and the sum in each group.

Besides these aggregate functions, you can also access specific elements based on their position or relative value within a group, using `first(), nth(n), last(), min(), median(), max()` etc.

You can also compute multiple functions in a single call using `g.agg(['min', 'max'])` or display a variety of statistical functions simultaneously with `g.describe()`.

## Difference between apply() and transform()
If above options are insufficient, you can pass the data through your custom Python function. It can be either:
* a function `f` that takes a group `x` (a Series object) and produces a single value (e.g., `sum()`) using `g.apply(f)`
* or a function `f` that takes a group `x` (a Series object) and generates a Series object with **the same size** as `x` (e.g., `cumsum()`) using `g.transform(f)`
    ```python
    import pandas as pd
  
    numbers = pd.Series([1, 3, 7, 9, 17, 23, 29])
    last_digits_gb = numbers.groupby(numbers % 10)
  
    print(f"numbers: {numbers.values}")
    print(f"numbers transformed: {last_digits_gb.transform(lambda x: x % 10).values}")
    print(f"numbers counting with apply(): {last_digits_gb.apply(lambda x: len(x)).values}")
    ```
    Output:
    ```
    numbers: [ 1  3  7  9 17 23 29]
    numbers transformed: [1 3 7 9 7 3 9]
    numbers counting with apply(): [1 2 2 2]
    ```
## groupby() with DataFrames
Firstly, with DataFrames you can indicate the column for grouping by simply using its name. In some cases, different columns may require distinct treatment during the grouping process. For instance, it is reasonable to calculate the sum for quantity, but not for price. By using the `.agg` method, you can designate unique aggregate functions for each column, as demonstrated in the example below: 
```python
import pandas as pd

data = {
    "City": ["London", "London", "New York", "New York", "New York", "Tokyo", "Tokyo"],
    "Category": ["Electronics", "Clothing", "Electronics", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Sales": [7000, 2000, 7000, 4000, 5000, 5000, 1000],
    "Offers": [70, 20, 10, 70, 40, 50, 50],
}

df = pd.DataFrame(data)
print(df.groupby('Category').agg(
    num_of_cities=('City', 'count'),
    min_sale=('Sales', 'min'),
    max_sale=('Sales', 'max'),
))
```
Output:
```
             num_of_cities  min_sale  max_sale
Category                                      
Clothing                 3      1000      5000
Electronics              4      4000      7000
```

Often the term "group by" denotes a process which could include one or more of the following stages:
 - Dividing the data into groups according to certain criteria
 - Executing a function independently on each group
 - Consolidating the outcomes into a data structure

## Task: simple analysis of sales data
You are given a dataset containing sales data for various products across different cities. Your goal is to answer the following questions:
1. What are the total sales for each city?
2. What are the average sales for each product category?
