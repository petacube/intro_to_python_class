## Common data issues: duplicates, missing values, inconsistencies

High data quality is essential for research and production, as it drives accurate decision-making, improves operational efficiency, enhances customer experience, and ultimately leads to better performance.

Let’s discuss some of the most common data quality issues and how we can tackle them with pandas. 

### 1. Duplicate data

As we saw in the previous task, data can come from different sources – local files and databases, cloud data storages, and streaming data. There is bound to be a lot of duplication in these sources.

The pandas method [DataFrame.duplicated()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#) returns boolean `Series` denoting duplicate rows.

```python
import pandas as pd

data = {
    'label': ['a', 'b', 'b', 'c', 'd', 'd']
}

df = pd.DataFrame(data)
duplicates = df.duplicated(keep='first')  # keep='first' marks duplicates as `True` except for the first occurrence
print(duplicates)
```
Output:
```text
0    False
1    False
2     True
3    False
4    False
5     True
dtype: bool
```

The method [DataFrame.drop_duplicates()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#) follows the same logic but returns a DataFrame with duplicate rows (the `True` ones) removed.

```python
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)
```
Output:
```text
  label
0     a
1     b
3     c
4     d
```

Using the optional parameter `subset` (column label or sequence of labels), you can also find or remove duplicates based on specific columns.

### 2. Missing values

Missing values are data missing in some fields or records. They can result from data entry errors, data collection problems, or the unavailability of information. Missing values can lead to biased or incomplete analyses and reduced model performance. 

Handling missing values typically involves either dropping rows/columns with missing data, filling them with a default value, or using techniques like interpolation and/or prediction of missing values.

### 3. Inconsistencies

Inconsistencies in data refer to discrepancies or irregularities in data values, formats, or representations. These can arise from human errors, system issues, or differences in data sources. To address inconsistencies, data cleaning and preprocessing techniques like standardizing units, transforming data types, and harmonizing data formats should be employed.

### Task
1. Get acquainted with the dataset sample and remove duplicates based on the `ID` column.
2. Identify and handle missing values in the `Age` column, replacing the gaps with the column mean.
3. Correct the inconsistencies in the `Height` column by converting all values to `float`.
