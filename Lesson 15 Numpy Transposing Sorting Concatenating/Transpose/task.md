## Transpose

When you transpose an array, the order of the axes is reversed, and the indices of each element are reversed along each axis.
Item `[0, 1]`, for example, becomes item `[1, 0]`.
[`numpy.ndarray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose) returns a view of the array with axes transposed.
Alternatively, you can also use the attribute [`a.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T).

This method accepts `None` or a tuple of `int`s. In the case of `None` or no argument, it reverses the order of the axes.
In the case of a tuple of `int`s, `i` in the `j`-th place in the tuple means that `a`’s `i`-th axis becomes `a.transpose()`’s `j`-th axis.
To illustrate it:

```python
a = np.arange(15).reshape(3, 5)
print(a.transpose())
print(a.T)
print(a.transpose(1, 0))
```
Output (all print the same thing):
```text
[[ 0  5 10]
 [ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]]
```

> <i>The method [`numpy.ndarray.reshape`](course://Numpy_/Array Basics/Reshape) we encountered earlier
gives a new shape to an array without changing its data and can also be used for transposing.</i>

<details>The transpose operation becomes more complex when dealing with arrays of higher dimensions, such as 3-D arrays. In the case of 3-D arrays, the transpose operation involves permuting the axes based on the provided axes parameter.</details>

### Task 
1. Transpose the array `a`.
2. Transform the array `b` so that it looks like this:
```text
   [[0 1 2]
   [3 4 5]
   [6 7 8]]
```
3. Use numpy methods `arange`, `reshape`, and `transpose` to acquire a 3D array `c` that looks like this:
```text
[[[ 0  4  8]
  [ 2  6 10]]

 [[ 1  5  9]
  [ 3  7 11]]]
```

<div class="hint">You can use either <code>a.T</code> or <code>a.transpose()</code> for the first two arrays.</div>

<div class="hint">In #3, use the methods in the suggested order. You can do it in one line of code.</div>
