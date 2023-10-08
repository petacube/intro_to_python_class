## Concatenate

Concatenation refers to joining two or more arrays of the same shape along a specified axis.
While there’s [`numpy.concatenate()`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html), there are also several helper functions 
that are sometimes easier to read.

`numpy.concatenate()` is used to join a sequence of arrays along an existing axis. It accepts 
a sequence of arrays of the same shape except in the dimension specified by the optional 
parameter `axis`, which is the axis along which the arrays will be joined. 
If `axis` is `None`, arrays are flattened before use. The default value is `0`. The function 
returns the concatenated array.

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[0, 0, 0]])
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b.T), axis=1))
print(np.concatenate((a, b), axis=None))
```
Output:
```text
[[1 2 3]
 [4 5 6]
 [7 8 9]
 [0 0 0]]
[[1 2 3 0]
 [4 5 6 0]
 [7 8 9 0]]
[1 2 3 4 5 6 7 8 9 0 0 0]
```
### Stack
1. [`numpy.stack()`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack) joins 
a sequence of arrays along a **new axis**. The `axis` parameter specifies the index of the new axis in 
the dimensions of the result. For example, if `axis=0`, it will be the first dimension, and if `axis=-1`,
it will be the last dimension.

```python
a = np.array([[1, 2], [3, 4]])
print(np.stack((a, a), axis=0))
print(np.stack((a, a), axis=-1))
```
Output:
```text
[[[1 2]
  [3 4]]
 [[1 2]
  [3 4]]]
  
[[[1 1]
  [2 2]]
 [[3 3]
  [4 4]]]
```
2. [`numpy.hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack) stacks
arrays in sequence horizontally (column-wise).
This is equivalent to concatenation along the second axis, except for 1D arrays, where it concatenates along the first axis:
```python
a, b = np.array((1, 2, 3)), np.array((4, 5, 6))
print(np.hstack((a, b)))
c, d = np.array([[1], [2], [3]]), np.array([[4], [5], [6]])
print(np.hstack((c, d)))
```
Output:
```text
[1 2 3 4 5 6]
[[1 4]
 [2 5]
 [3 6]]
```
3. [`numpy.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack) stacks
arrays in sequence vertically (row-wise). This is equivalent to concatenation along the first axis after 
1D arrays of shape `(N,)` have been reshaped to `(1, N)`.
```python
a, b = np.array((1, 2, 3)), np.array((4, 5, 6))
print(np.vstack((a, b)))
c, d = np.array([[1], [2], [3]]), np.array([[4], [5], [6]])
print(np.vstack((c, d)))
```
Output:
```text
[[1 2 3]
 [4 5 6]]
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
```

### Task
1. You are given an array of zeros `a` of the shape `(3, 4)`. Create an array `b` such that
when you concatenate it appropriately with `a`, you get:
```text
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [0 1 2 3]]
```
2. Use one of the stacking methods to create an array `stacked`:
```text
[[ 0  1  2  3  4  5  6  7  8  9]
 [20 21 22 23 24 25 26 27 28 29]
 [40 41 42 43 44 45 46 47 48 49]]
```
<div class="hint">Use <code>np.arange</code> for <code>b</code> and do not forget to 
reshape the array appropriately! Also, mind the concatenation axis.</div>
<div class="hint">The task with <code>stacked</code> can be completed in one line. Use <code>np.arange</code> for
each of the three initial arrays.</div>