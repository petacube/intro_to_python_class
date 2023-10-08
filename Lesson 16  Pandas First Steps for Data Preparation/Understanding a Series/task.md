## Understanding a Series
In this task, we'll introduce a Series — the first of two main data structures at the core of pandas. 

A [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series) is a one-dimensional labeled array. 
It is homogenous and size-immutable, i.e., a Series' elements must be of the same data type, and once created, 
the size of a Series object cannot be changed. You can also see it as the primary building block for a DataFrame, 
making up its rows and columns. We'll explore the key properties of DataFrame in the following tasks. 

A Series is capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).
The axis labels are collectively referred to as the `index`. The basic method to create a Series is to call:
```python
s = pd.Series(data, index=index)
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
