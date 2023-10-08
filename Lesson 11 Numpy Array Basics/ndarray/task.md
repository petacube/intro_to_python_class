## ndarray

At the core of the NumPy package is the [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) object – a homogeneous multidimensional array.
`ndarray` is a shorthand for "N-dimensional array". An N-dimensional array is simply an array with any number of dimensions.
It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. 
In NumPy, dimensions are called axes.

In the example below, the array `arr` has 2 axes. The first axis has 
a length of 2, the second one has a length of 3.

```text
[[1., 0., 0.],
 [0., 1., 2.]]
```

Axes are numbered starting from 0. The 0th axis is a row, and the 1st axis is a column.
To access the elements, you have to specify their coordinates along each axis while following the order of the axes. 
For example, to access the number `2.` from the array above, you should use `arr[1, 2]`.

`ndarray` is also known by the alias `array`. 
Note that `numpy.array` is different from the Standard Python Library class `array.array`, 
which can only handle one-dimensional arrays and offers way less functionality. Some of the 
important attributes of an `ndarray` object are:

- [`ndarray.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html) – the number of axes (dimensions) of the array.

- [`ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html) – the dimensions of the array: a tuple of integers indicating the size of the 
  array in each dimension. The `shape` of a matrix with `3` rows and `5` columns will 
  be `(3, 5)`. The length of the `shape` tuple is the number of axes, `ndim`.

- [`ndarray.size`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html) – the total number of elements in the array. Equals the 
  product of the elements of `shape`.

- [`ndarray.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html) –  an object describing the type of the elements in the array. 
  One can create or specify dtype’s using standard Python types. Additionally, NumPy 
  provides types of its own: `numpy.int32`, `numpy.int16`, and `numpy.float64` are some examples.

Run the code in `main.py` to see some examples in the output.
To run this script, right-click anywhere in the **Editor** view so you can see the context 
menu and select **Run 'script_name'**. Alternatively, you can use the &shortcut:RunClass; shortcut
or the ![](execute.svg) gutter icon. 

<style>
img {
  display: inline !important;
}
</style>