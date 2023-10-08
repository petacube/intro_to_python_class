## Understanding a DataFrame

[pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) is a two-dimensional labeled tabular structure. It is potentially heterogenous and size-mutable.
You can think of it like a spreadsheet or SQL table, or a dict of Series objects. 
It is generally the most commonly used pandas object. 

Like Series, DataFrame accepts many different kinds of input:
- A 2D [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) object
- A Dict of 1D ndarrays, lists, dicts, or Series
- A structured or record ndarray
- A Series
- Another DataFrame

Along with the data, you can optionally pass `index` (row labels) and `columns` (column labels) arguments. 
If you pass an index and/or columns, you are guaranteeing the index and/or columns of the resulting DataFrame. 
Thus, a dict of Series plus a specific index will discard all data not matching up to the passed index.
If axis labels are not passed, they will be constructed from the input data based on common sense rules.

Below are some examples of creating DataFrames.

### From a list of namedtuples
The field names of the first [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple) in the list determine the columns of the DataFrame. The remaining namedtuples (or tuples) are simply unpacked and their values are fed into the rows of the DataFrame. If any of those tuples is shorter than the first namedtuple, then the later columns in the corresponding row are marked as missing values. If any are longer than the first namedtuple, a `ValueError` is raised.
```python
import pandas as pd
from collections import namedtuple

Point = namedtuple("Point", "x y")

print(pd.DataFrame([Point(0, 0), Point(0, 3), (2, 3)]))
```
Output:
```text
   x  y
0  0  0
1  0  3
2  2  3
```

### From a list of dataclasses
Data Classes as introduced in [PEP557](https://www.python.org/dev/peps/pep-0557) can be passed into the DataFrame constructor. Passing a list of dataclasses is equivalent to passing a list of dictionaries.

Please be aware that all values in the list should be dataclasses; mixing types in the list would result in a `TypeError`.
```python
import pandas as pd
from dataclasses import make_dataclass

Point = make_dataclass("Point", [("x", int), ("y", int)])

print(pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)]))
```
Output:
```text
   x  y
0  0  0
1  0  3
2  2  3
```

### Alternate constructors

If necessary, you can use other similar constructors to create DataFrames, such as [DataFrame.from_dict](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict) or [DataFrame.from_records](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records). These, as well as other options, are detailed in the [pandas documentation](http://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).
