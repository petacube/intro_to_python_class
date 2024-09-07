## introducing Pandas, Polars and PySpark

We are are going to primarily study pnadas but 
We will also study in parallel libraries called polars and pyspark 
they are sister libraries - implement same functionality slighly differently 
- but polars is much faster than pandas
however, polars does not support index functionality
simular pyspark is also open-source software for doing 
very large data processing at scale. 

here is the comparison of the three libraries

|                      | pandas              | polars                      | pyspark                                    |
|----------------------|---------------------|-----------------------------|--------------------------------------------|
| **when to use**      | data < 100MB        | data < 100GB                | data > 100GB                               |
| **Parallel & distributed** | limited (with dask) | parallel                    | parallel and distributed                   |
| **technology**       | python/numpy/arrow  | python/Rust/arrow           | python/Java/arrow                          |
| **performance**      | slow                | fast                        | medium                                     |
| **Features – select/join/group** | yes                 | yes                         | yes                                        |
| **User-defined-functions** | yes, python         | yes, python & Rust          | yes, python                                |
| **cost**             | free                | Free & commercial           | free (apache spark) and commercial (databricks) |

All three libraries are used in Data Engineering - the goal is to take unstructured data 
and convert into structured form - numpy arrays and apply linear algebra analytics. 

## Understanding a Series
In this task, we'll introduce a Series — the first of two main data structures at the core of pandas. 


A [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series) is a one-dimensional labeled array. 
It is homogenous and size-immutable, i.e., a Series' elements must be of the same data type, and once created, 
the size of a Series object cannot be changed. You can also see it as the primary building block for a DataFrame, 
making up its rows and columns. We'll explore the key properties of DataFrame in the following tasks. 

A Series is capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).
The axis labels are collectively referred to as the `index`. The basic method to create a Series is to call:
```python
import pandas as pd
import polars as pl
fname = r"C:\Users\stani\work\intro_python2\intro_to_python_class\Lesson 16  Pandas First Steps for Data Preparation\Understanding a Series\NVDA.csv"

df = pd.read_csv(fname)
df.set_index("Date",inplace=True)
df.loc["2023-08-30"]
pl_df = pl.read_csv(fname)


#s = pd.Series(data, index=index)
s= df["Open"]
s_pl = pl_df["Open"]

#create series using lists and index
stock_ibm = pd.Series([1,2,3,4,5],index=["Jan","Feb","Mar","Apr","May"])
stock_ibm["Jan"]

# stock multiplied
# notice how indexes are preserved
stock_ibm_mult = stock_ibm.apply(lambda x: x**2)

stock_ibm.value_counts()

stock_ibm.rolling(2).mean()
```
Here, `data` can be many different things:
- a 1D [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) object
- an array-like (list, tuple, etc.) or an Iterable
- a scalar value (like 7)
- a Python dict

The passed `index` is a list of axis labels. 

A Series acts very similarly to a `numpy.ndarray` and is a valid argument to most NumPy functions. However, operations such as slicing will also slice the index. If you need an actual `ndarray`, then use the [Series.to_numpy()](http://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy) method.

Run the code in `task.py` to see some examples in the output.
To run this script, right-click anywhere in the **Editor** view so you can see the context 
menu and select **Run 'script_name'**. Alternatively, you can use the &shortcut:RunClass; shortcut
or the ![](execute.svg) gutter icon. 

<style>
img {
  display: inline !important;
}
</style>
