## Integer Array Indexing

NumPy arrays may be indexed with other arrays.
For all cases of index arrays, what is returned is a copy of the original data, not a view as one gets for slices.

Index arrays must be of integer type. Each value in the array indicates which value in the array 
to use in place of the index. Negative values are permitted and work as they do with single indices or slices.

```python
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a = np.array([0, 3, 5, 2])
print(x[a])
```
Output:
```text
[1 4 6 3]
```

When index arrays are used, what is returned is an array with the same shape as the index 
array, but with the type and values of the array being indexed:
```python
b = np.array([[9, 9], [0, 1]])
c = x[b]
print(c)
```
Output:
```text
[[10 10]
 [ 1  2]]
```

### Indexing multidimensional arrays
Things become more complex when multidimensional arrays are indexed, particularly with multidimensional index arrays.
Let's consider this:

```python
x = np.arange(15).reshape(5, 3)
print(x)
print(x[np.array([0, 1, 4])])  # 1
print(x[np.array([0, 1, 4]), np.array([0, 0, 1])])  # 2
```
Output:
```text
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]
 [12 13 14]]
 
[[ 0  1  2]
 [ 3  4  5]
 [12 13 14]]
 
[ 0  3 13]
```
You can see that in the first case, a new array is constructed, where 
each value of the index array selects one row from the indexed array and the resulting 
array has the shape `(number_of_index_elements, size_of_row)`.

In the second case, the resulting array has the same shape as the index arrays, and the values 
correspond to the index set for each position in the index arrays. In this example, the first 
index value is `0` for both index arrays, and thus the first value of the resulting array is `x[0, 0]`. 
The next value is `y[1, 0]`, and the last one is `y[4, 1]`.

If the index arrays do not have the same shape, an attempt is made to broadcast them to the same shape. 
If they cannot be broadcast to the same shape, an exception is raised.

The broadcasting mechanism permits index arrays to be combined with scalars for other indices. 
The scalar value is used for all the corresponding values of the index arrays:

```python
x = np.arange(15).reshape(5, 3)
print(x[np.array([0, 2, 3, 4]), 1])
```
Output:
```text
[ 1  7 10 13]
```
You can read more about integer indexing [here](https://numpy.org/doc/stable/reference/arrays.indexing.html#integer-array-indexing).

### Task
1. Using integer array indexing, create an array `a` that contains elements with 
   indices `[7, 13, 28, 33]` from the array `x`.
   Then create a 2D array `b` with the shape `(3, 3)` that contains elements with indices
   `[0, 1, 2], [10, 11, 12], [28, 29, 30]` from the array `x`.
   
2. Based on the 2D array `y`:
   - Create an array `c` containing rows number `0`, `2`, and `4`.
   - Create a 1D array `d` containing elements `0`, `1`, and `2` from the rows `0`, `2`, and `4`, respectively.
   - Create a 1D array `e` containing elements with the index `6` from rows `1`, `2`, and `4`.
    
