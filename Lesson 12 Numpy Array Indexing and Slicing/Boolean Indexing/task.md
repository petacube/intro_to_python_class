## Boolean Indexing

Boolean arrays used as indices are treated differently from index 
arrays. Boolean arrays must be of the same shape as the initial dimensions of the array being indexed.
Such boolean arrays are often referred to as **masks**, and the process of using them in indexing other arrays
is called masking or masked filtering.

```python
y = np.arange(20).reshape(5, 4)
b = y % 2 != 0
print(b)
print(y[b])
```
Output:
```text
[[False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True False  True]]
[ 1  3  5  7  9 11 13 15 17 19]
```
Unlike in the case of integer index arrays, in the boolean case, the result is a 1D array 
containing all the elements in the indexed array corresponding to all the true elements in the boolean array.
As with index arrays, what is returned is a copy of the data, not a view as one gets with slices.


The result will be multidimensional if `y` has more dimensions than `b`. For example, if we use a
1D boolean array where the second dimension agrees with that of `b` (just selecting one row from `b`),
then the columns from `y` corresponding to the `True` values in the 1D array will be selected:
```python
print(b[1, :])
print(y[:, b[1, :]])
```
Output:
```text
[False  True False  True]
[[ 1  3]
 [ 5  7]
 [ 9 11]
 [13 15]
 [17 19]]
```
The 2nd and 4th columns are selected from the indexed array and combined to make a 2D array.

In general, when the boolean array has fewer dimensions than the indexed array,
the shape of the result is one dimension containing the number of `True` elements 
of the boolean array followed by the remaining dimensions of the indexed array.

For further details, consult the NumPy reference documentation on [array indexing](https://numpy.org/doc/stable/reference/arrays.indexing.html#indexing).

### Task 
1. Create a 3D array `a` with integers from 0 to 19 and the shape `(2, 2, 5)`.
2. Filter it using a 2D boolean array `b` so that the resulting 2D array `c` has the
shape `(2, 5)` and contains elements `[ 0  1  2  3  4]` and `[15 16 17 18 19]`.