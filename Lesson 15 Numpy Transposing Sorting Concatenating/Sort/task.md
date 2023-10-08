## Sort

Methods [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html?highlight=sort#numpy.sort) 
and [`numpy.ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort) can both be used to sort an array, 
the only difference being that the former returns a sorted copy of an array, while the latter is used 
to sort in-place.

<details>

Various sorting algorithms can be used with these methods (see the documentation); they differ in 
their average speed, worst-case performance, work space size, and stability.
The default is [quicksort](https://en.wikipedia.org/wiki/Quicksort).
</details> 

```python
a = np.array([[1, 4], [3, 1]])
print(np.sort(a))               # Sorts along the last axis by default. Returns a copy!
print(np.sort(a, axis=None))     # Sorts the flattened array
print(np.sort(a, axis=0))       # Sorts along the first axis
```
Output:
```text
[[1 4]      
 [1 3]]
[1 1 3 4]  
[[1 1]      
 [3 4]]
```
On the other hand, if we use `numpy.ndarray.sort`, we get:
```python
a = np.array([[1, 4], [3, 1]])
a.sort(axis=1)      # Sorts in-place along the second axis. Equivalent to `a.sort()`
print(a)
a.sort(axis=0)      # Sorts in-place along the first axis
print(a)
```
Output:
```text
[[1 4]
 [1 3]]
[[1 3]
 [1 4]]
```
The difference in the results comes from the fact that the first method `numpy.sort` returns a copy of an array, while
the second one (`numpy.ndarray.sort`) modifies the initial array. That is, in the exapmle above, we sort the elements of one array, first inside the rows, then inside the columns.

### Indirect sort
As opposed to the methods discussed above, the [`numpy.argsort()`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort) method returns the **indices**
that would sort an array. 
It performs an indirect sort along the given axis and returns an array of indices (of the 
same shape as the input array) that index data along the given axis in sorted order.

For a 1D array:
```text
x = np.array([3, 1, 2])
print(np.argsort(x))
```
Output:
```text
[1 2 0]
```
For a 2D array:
```python
y = np.array([[0, 3], [2, 1]])
ind = np.argsort(y, axis=0)  # Sorts along the first axis (down)
print(ind)
print(np.take_along_axis(y, ind, axis=0))  # Same as np.sort(x, axis=0)
```
Output:
```text
[[0 1]
 [1 0]]
[[0 1]
 [2 3]]
```
Continuing the last example:
```python
ind2 = np.argsort(y, axis=1)  # Sorts along last axis (across)
print(ind2)
print(np.take_along_axis(y, ind2, axis=1))  # Same as np.sort(x, axis=1)
```
Output:
```text
[[0 1]
 [1 0]]
[[0 3]
 [1 2]]
```
`argsort` is a frequently used sorting functionality in data-intensive code work. It increases the speed of 
computation, especially when the datasets are very large.

The function [`numpy.take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html)
takes values from the input array using an index array. This is needed whenever you
work with NumPy functions such as `argsort`, [`argpartition`](course://Numpy/Transposing Sorting Concatenating/Partial Sort), and [`argmax`](course://Numpy/Compare Search/Find maximum), which 
return an array of indices that can be further used to sort the initial array or perform some other operation
with it.

### Task
You are given a 2D array of 100 random integers.
1. Sort the columns (second axis!) of this array and assign the result to the variable `b`.
2. Find indices to sort the rows of the array `b` and assign the result to `ind`.
3. Fully sort the array by using those indices. Check out the examples above.