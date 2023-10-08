## Create a Series

There are several ways you can create a Series.

* First, you can create a Series from a regular Python list, 1D `numpy.ndarray`, or other iterable object using the constructor `pandas.Series()`. 
The type of the resulting array will be deduced from the type of the elements in the source sequences.

      import pandas as pd

      a = pd.Series([0, 1, 2])
      b = pd.Series(("0", "1", "2"))

      print(a.dtype)
      print(b.dtype)

  Output:
  ```text
  int64
  object
  ```

* Second, you can use a scalar value:

      import pandas as pd

      print(pd.Series(7, index=range(3)))

  Output:
  ```text
  0    7
  1    7
  2    7
  dtype: int64
  ```

* Third, you can create a Series from a Python dict.
 
### Task
Complete the implementation of the function `create_series(dict_: dict)` so that it creates a Series from a Python dict.
