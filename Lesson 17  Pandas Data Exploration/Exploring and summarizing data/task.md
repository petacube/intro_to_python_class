Exploring data is an important first step in any data analysis project. 
Pandas provides a variety of tools for exploring and summarizing data, 
including `describe()`, `info()` and `shape`.
These functions allow you to 
quickly understand the size and structure of your dataset, as well as basic 
statistics like mean, standard deviation and quartiles.

### `describe()`

The `describe()` function in pandas provides a comprehensive summary of numerical and 
categorical data. It calculates statistics like count, mean, standard deviation, 
minimum, maximum, quartiles and more. It helps understand data distribution, 
identify outliers and check for missing values.

`describe()` works with different data types and have different statistics for each data type.

Basic syntax:
```python
data_frame.describe(percentiles=None, include='all')
```

Example:
```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                   'numeric': [1, 2, 3],
                   'object': ['a', 'b', 'c']
                  })
df.describe()  # By default only numeric columns are included
df.describe(include='all')  # include all columns
df.describe(include=[object])  # include only object columns
```

### `info()`
Returns the description of every column (it's type, non-null counts and memory usage).

Basic syntax:
```python
data_frame.info(verbose=True, memory_usage=True)
```

Example:
```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                   'numeric': [1, 2, 3],
                   'object': ['a', 'b', 'c']
                  })
df.info(verbose=True, memory_usage=True)
```

### `value_counts()`
Returns the counts of unique rows on the DataFrame. If you specify the row, 
it will return the counts of unique values in that row.

Basic syntax:
```python
data_frame.value_counts(subset=None)
```

Example:
```python
import pandas as pd

df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Dolly', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Brown', 'Blake', 'Andreou', 'Smith']
                  })
df.value_counts()  # get unique row count 
df.value_counts(subset='surname')  # get unique value counts for row 'surname'
```


### Computing basic statistics

Pandas have a bunch of built-in functions to compute different statistics. There are some helpful functions to explore your data.
- `df.shape()` – returns the shape of the dataframe
- `df.mean(axis=None, skip_na=True)` – returns mean over specified axis (defaut axis – columns)
- `df.mode(axis=None)` – returns mode over specified axis
- `df.min(axis=None, skip_na=True)` – returns min over specified axis
- `df.max(axis=None, skip_na=True)` – returns max over specified axis
- `df.sum(axis=None)` – returns sum of all values over specified axis
- `df.std(axis=None)` – returns standart deviation over specified axis
- `df.var(axis=None)` – returns variance over specified axis

   _Statistical note: for Series and DataFrame objects, `var()` normalizes by `N-1` 
   to produce unbiased estimates of the variance, while NumPy’s `numpy.var()` 
   normalizes by `N`, which measures the variance of the sample. 
   Also note that `cov()` normalizes by `N-1` in both Pandas and NumPy._
 
- `df.cov()` – returns covariance table for each pair of columns
- `df.quantile(q=[0.1, 0.5])` – returns the specified quantiles


