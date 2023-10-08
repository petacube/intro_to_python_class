## Create and manipulate a DataFrame

In this task, you will create a DataFrame using different input types and perform basic operations to better understand the DataFrame structure.


```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['Saint Petersburg', 'New York', 'Prague', 'Paphos']
}

print(pd.DataFrame(data))
```
Output:
```text
      Name  Age              City
0    Alice   25  Saint Petersburg
1      Bob   30          New York
2  Charlie   35            Prague
3    David   40            Paphos
```

### Working with columns

You should use the indexing operator `[]` to select columns, perform boolean indexing, or slice rows.

```python
column_age = df['Age']  # Select a single column, the result is Series
print(column_age)
```
Output:
```text
0    25
1    30
2    35
3    40
Name: Age, dtype: int64
```

```python
columns_name_age = df[['Name', 'Age']]  # Select multiple columns, the result is DataFrame
print(columns_name_age)
```
Output:
```text
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   35
3    David   40
```

```python
rows_1_to_2 = df[1:3]  # Select rows by number, the result is DataFrame
print(rows_1_to_2)
```
Output:
```text
      Name  Age      City
1      Bob   30  New York
2  Charlie   35    Prague
```

Keep in mind that applying the `[]` operator directly on a DataFrame is primarily used for column selection and basic row slicing. For more advanced row selection or selecting both rows and columns simultaneously, you should use the `.loc[]` and `.iloc[]` functions provided by Pandas.

### Boolean indexing

```python
rows_age_gt_30 = df[df['Age'] > 30]  # Select rows where the values in column 'Age' are greater than 30

print(rows_age_gt_30)
```
Output:
```text
      Name  Age    City
2  Charlie   35  Prague
3    David   40  Paphos
```

### Selection by callable
Now comes the fun and brain-bending part: passing in a function for indexing. That may come in very handy when you are chaining operations and the index has different values. It is very common with grouping operations, which we will see later in the course.

Here is an example of passing in a function that filters the rows where the values in the `Age` column are greater than 30:

```python
def age_filter(dataframe):
    return dataframe['Age'] > 30

rows_age_gt_30 = df[age_filter]  # Select rows where the values in column 'Age' are greater than 30
print(rows_age_gt_30)
```
Output:
```text
      Name  Age    City
2  Charlie   35  Prague
3    David   40  Paphos 
```

You can also create a function that returns a filter function:
```python
def create_filter(column, threshold):
    def _filter(dataframe):
        return dataframe[column] > threshold
    return _filter

age_filter = create_filter('Age', 30)
rows_age_gt_30 = df[age_filter]  # Select rows where the values in column 'Age' are greater than 30
```

### Task
1. Add a new column called `Month cost` to the DataFrame with the following values: `[50000, 800000, 200000, 500000]`.
2. Compute the `Annual cost in thousands` and add this column to the DataFrame.

<div class="hint">You can operate with the columns as if they were just numbers. Also, use the int64 type for the column `Annual salary in thousands`.</div>
