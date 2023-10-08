### `sort_values()`

 To sort values in a pandas DataFrame, you can use the `sort_values()` method and 
 specify the index/column(s) you want to sort by. By default, the sort_values() method 
 sorts in ascending order, but you can set the ascending parameter to False for descending order.
  Additionally, you can sort by multiple columns by passing a list of column names 
 to the 'by' parameter.
 
Basic syntax:
```python
data_frame.sort_values(by=['column_1'], ascending=True, inplace=False)
```

Example:
```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                   'numeric': [2, 1, 3, 1],
                   'object': ['a', 'c', 'b', 'b']
                  })

df.sort_values(by=['numeric'])  # sort by 'numeric' column 
df.sort_values(by=['numeric', 'object'], ascending=False)  # sort descending firstly by 'numeric' then by 'object' columns
```

## Task

Sort people in the dataframe by the surname in the descending order. 
People with the same surname should be sorted according to their age.