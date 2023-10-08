## Basic indexing with .loc[] and .iloc[]

In Pandas, `.loc[]` and `.iloc[]` are powerful indexing functions that allow you to select and manipulate data in a DataFrame based on labels (for .loc[]) or index positions (for .iloc[]).

### .loc[]

The `.loc[]` function is a label-based data selecting method, which means you have to pass the row and column labels to select data from a DataFrame.

Basic Syntax:
```python
data_frame.loc[row_labels, column_labels]
```
Example:
```python
import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])

row = df.loc['row1']  # Select a single row by label

rows = df.loc[['row1', 'row3']]  # Select multiple rows by labels

cell = df.loc['row1', 'B']  # Select a single cell by row and column labels

subset = df.loc[['row1', 'row3'], ['A', 'C']]  # Select multiple rows and columns by labels

subset_with_slices = df.loc['row1':'row2', 'A':'B']  # Select multiple rows and columns by labels
```
**Note** that unlike the case of regular Python slices, both the start and the stop are included when present in the index!

### .iloc[]

The `.iloc[]` function is an integer position-based indexing method, which means you have to pass integer index values to select data from a DataFrame.

Basic Syntax:
```python
data_frame.iloc[row_indices, column_indices]
```
Example:
```python
import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

row = df.iloc[0]  # Select a single row by index

rows = df.iloc[[0, 2]]  # Select multiple rows by indices

cell = df.iloc[0, 1]  # Select a single cell by row and column indices

subset = df.iloc[[0, 2], [0, 2]]  # Select multiple rows and columns by indices
```
**Remember** that with .iloc[], the ending index is exclusive.

In conclusion, understanding the differences and appropriate use cases for `.loc[]` and `.iloc[]` will allow you to work with `pandas.DataFrame` more effectively and efficiently.
