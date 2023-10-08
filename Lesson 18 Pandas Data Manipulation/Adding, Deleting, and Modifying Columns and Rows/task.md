# Adding, Deleting, and Modifying Columns and Rows of a DataFrame
## Adding a Column
To add a new column to a DataFrame, simply assign a new Series or a list of values to a new column name.
```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
}

df = pd.DataFrame(data)
df["City"] = ["London", "New York", "Tokyo", "Berlin"]
```
Because a DataFrame is composed of columns, performing operations on rows is somewhat more complex than on columns. For instance, when inserting a column (see [pd.DataFrame.insert()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html)), the operation is done in-place, whereas adding a row always generates a new DataFrame.

## Deleting a Column
You can delete columns using the `drop()` method, specifying the axis and the column name.
```python
df = df.drop("City", axis=1)

# Alternatively, you can use the del keyword.
del df["City"]
```

## Modifying a Column
To modify a column, you can simply perform operations on the existing column and assign the result back to the column.
```python
df["Age"] = df["Age"] + 1
```

## Adding and Deleting Rows
To add a new row, you can use either inplace assignment with `loc`: 
```python
new_row = {"Name": "Eva", "Age": 45}
df.loc[len(df.index)] = new_row
```
Or the `ps.concat()` method, which we will discuss later.

To delete a row, use the `drop()` method with the index value of the row and the axis.
```python
df = df.drop(4, axis=0)
```

## Modifying Rows
To modify a row, use the loc or iloc attributes to access the row and assign new values.
```python
df.loc[3, ["Name", "Age"]] = ["Diana", 38]
```

## `SettingWithCopy` warning
It's time to handle with legendary `SettingWithCopy` warning. When working with pandas DataFrames, it is important to understand the difference between a view and a copy. 

A **view** is a reference to the original data, meaning any modifications made to the view will also affect the original data. In other words, a view is a "window" into the same underlying data without creating a separate object.

A **copy**, on the other hand, is a separate object that contains a duplicate of the original data. Changes made to the copy do not affect the original data. 

When you use indexing or slicing operations in pandas, sometimes it returns a view, and sometimes it returns a copy. The behavior depends on the specific operation and the memory layout of the DataFrame. Pandas issues a "SettingWithCopyWarning" when it detects that you might be trying to modify a copy of the data, while you probably intended to modify the original data. This warning is meant to help you avoid unintentional side effects.

To prevent this warning and ensure you are working with the correct object, you can use the `.copy()` method to explicitly create a copy of the DataFrame when you need one. Alternatively, you can use `.loc[]`, `.iloc[]`, or `.at[]` when you want to modify the original DataFrame in-place.

Keep in mind that the `SettingWithCopy` warning is just a warning and not an error. It serves as a reminder to double-check your code and make sure you are working with the intended DataFrame (original or copy).

## Task
1. Add a new column `Country` with the values ["UK", "USA", "Japan", "Germany"].
2. Delete the `City` column.
3. Increase the ages of all people by 1.
4. Add a new row with the data ["Eva", 45, "Germany"].
5. Delete the row with index 2.
6. Modify the row with index 1 to have the name "Robert" and age 32.
