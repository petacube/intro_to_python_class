Pandas have some build-in methods that would be perfect for simple and fast visualization, 
including line plots, bar plots, scatter plots, histograms, box plots, and more. 

### `hist()`

Make a histogram of the DataFrame’s columns.

Basic syntax:
```python
data_frame.hist(bins=a)
```

Example:
```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f', 'e']),
                   'numeric': [1, 2, 3, 2],
                   'object': ['a', 'b', 'c', 'c']
                  })
df.bins(bins=3)
```

### `boxplot()`

Make a boxplot from DataFrame’s columns. There are different usage examples.

- Boxplots can be created for every numeric column in the dataframe by df.boxplot()
 or indicating the columns to be used

```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f', 'e']),
                   'numeric': [1, 2, 3, 2],
                   'numeric_2': [0, 0, 1, 2],
                   'object': ['a', 'b', 'c', 'c']
                  })
df.boxplot(column=['numeric', 'numeric_2'])
```

- Boxplots of variables distributions grouped by the values of a third variable.
```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f', 'e']),
                   'numeric': [1, 2, 3, 2],
                   'numeric_2': [0, 0, 1, 2],
                   'object': ['a', 'b', 'c', 'c']
                  })
df.boxplot(by=['object'])
```
- Boxplots of variables distributions grouped by the values of a third variable only 
for specified numeric columns.                                                                                                                                                       .
```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f', 'e']),
                   'numeric': [1, 2, 3, 2],
                   'numeric_2': [0, 0, 1, 2],
                   'object': ['a', 'b', 'c', 'c']
                  })
df.boxplot(by=['object'], column=['numeric'])
```


### `plot()`

Pandas offers a wide range of plotting methods that allow you to create different types of visualizations, 
including line plots, bar plots, scatter plots, histograms, box plots, and more. These methods are accessed using the 
`.plot()` function, which can be applied directly to a DataFrame or Series.

You can check documentation for all supported functions.

```python
import pandas as pd

df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Dolly', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Brown', 'Blake', 'Andreou', 'Smith'],
                   'age': [23, 45, 12, 22, 73, 34, 45],
                   'height': [178, 183, 150, 163, 158, 178, 167],
                   'favourite_colour': pd.Categorical(['blue', 'red', 'green', 'yellow', 'pink', 'yellow', 'red'])})

# Create a bar plot of sales by product category
df.plot(x='favourite_colour', y='age', kind='bar')

# Create a scatter plot of sales against advertising spend
df.plot(x='age', y='height', kind='scatter')

# Create a histogram of the distribution of ages
df['age'].plot(kind='hist')

# Create a Kernel Density Estimate plot of height
df['height'].plot(kind='kde')

```