# Merging and Combining Data
In this lesson, we will learn about combining and merging data using `pandas`. Often, you need to combine data 
from multiple sources to perform a comprehensive analysis. Pandas provides several methods to combine DataFrames, 
such as `concat()`, `merge()`, and `join()`. We will explore these methods and understand how to use them effectively.

## Concat
[pd.concat()](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) is used to concatenate DataFrames 
along a particular axis (either rows or columns). By default, it concatenates DataFrames vertically (along rows).
```python
import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']})

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                    'B': ['B3', 'B4', 'B5']})

vstack = pd.concat([df1, df2], ignore_index=True)
print(vstack)
```
Output:
```
    A   B
0  A0  B0
1  A1  B1
2  A2  B2
3  A3  B3
4  A4  B4
5  A5  B5
```
If the columns in the DataFrames do not align perfectly (disregarding the order), Pandas can either take the intersection of the columns (using `join='inner'`, which is the default) or insert NaNs to represent the missing values (using `join='outer'`).

`pd.concat()` may also perform "horizontal" stacking, which is similar to `hstack()` in NumPy.
```python
hstack = pd.concat([df1, df2], axis=1, keys=['df1', 'df2'])
print(hstack)
```
Output:
```
  df1     df2    
    A   B   A   B
0  A0  B0  A3  B3
1  A1  B1  A4  B4
2  A2  B2  A5  B5
```

## Merge
[pd.DataFrame.merge()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) is used to merge 
DataFrames based on a common column (or index). It is similar to a SQL join operation. So if the column you want 
to merge on is not in the index, use merge.
```python
import pandas as pd

# Sample DataFrames
users = pd.DataFrame({'user_id': [1, 2, 3],
                      'name': ['Alice', 'Bob', 'Charlie']})

orders = pd.DataFrame({'user_id': [1, 2, 1, 3],
                       'item': ['Book', 'Pen', 'Pencil', 'Eraser'],
                       'quantity': [1, 3, 2, 1]})

merged_df = users.merge(orders, on='user_id')
print(merged_df)
```
Output:
```
   user_id     name    item  quantity
0        1    Alice    Book         1
1        1    Alice  Pencil         2
2        2      Bob     Pen         3
3        3  Charlie  Eraser         1
```

The `merge()` method disregards any existing index values. Following that, it performs the join operation. 
Ultimately, it renumbers the results from `0` to `n-1`.

## Join
If the column is already present in the index of the DataFrames, you may use the `join()` method (which is essentially an alias for `merge()` with `left_index` or `right_index` set to `True` and different default settings). [pd.DataFrame.join()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html) is used to join DataFrames based on their index values. By default, it performs a left join, but other join types (inner, outer, right) are also supported.
```python
import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']},
                    index=['I0', 'I1', 'I2'])

df2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                    index=['I0', 'I2', 'I3'])

df1_join_df2 = df1.join(df2, how='outer')
print(df1_join_df2)
```
Output:
```
      A    B    C    D
I0   A0   B0   C0   D0
I1   A1   B1  NaN  NaN
I2   A2   B2   C2   D2
I3  NaN  NaN   C3   D3
```

## Combine
The [pandas.DataFrame.combine()]((https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html)) method is used to combine two DataFrames element-wise, with an custom function applied to each pair of elements.
```python
import pandas as pd

df1 = pd.DataFrame({"A": [1, 2, None], "B": [4, 5, 6]})
df2 = pd.DataFrame({"A": [None, 2, 3], "B": [4, None, 6]})


def take_smaller(s1, s2):
    return s1 if s1.sum() < s2.sum() else s2


# Combine DataFrames
combined = df1.combine(df2, take_smaller)
print(combined)
```
Output:
```
     A    B
0  1.0  4.0
1  2.0  NaN
2  NaN  6.0
```

## Task
1. Merge the two DataFrames `licenses_df` and `import_statements_df` on the `project_name` column.
2. Filter the merged DataFrame to only include projects with the specified licenses
['Apache License 2.0', 'MIT License'].
3. Count the number of imports of different libraries for projects under the specified licenses.

<div class="hint">
  You should use `pd.DataFrame.isin()` method for the second step.
</div>
<div class="hint">
  And also you may use `pd.DataFrame.value_counts()` for the third one.
</div>
