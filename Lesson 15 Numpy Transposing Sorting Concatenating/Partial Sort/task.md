## Partial Sort (Partition)

If you have some dataset in the form of a numpy array and you only want to get `k` smallest numbers from it instead of fully sorting it,
this task can be performed using the [`numpy.partition()`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition) method.
This is called **partial sort** because we will actually be sorting only some parts of the array, 
which means we will be getting a **partition** of `k` smallest values.

`numpy.partition()` creates a copy of the array with its elements rearranged in such a way that the element in the
k-th position is where it would be in a sorted array. All elements smaller than the k-th element 
are moved before this element, and all **equal or greater** are moved behind it. The ordering of the elements 
in the two partitions is undefined.

The method accepts the array to be sorted and an element index to partition it by.
In the example below, the dataset of 10 integers is partitioned by the 5th element:

```text
a = np.array([6, 0, 5, 2, 17, 2, 10, 17, 0, 13])
b = np.partition(a, 4)
print(a, '\n', b)
```
Output (the ^ sign indicates the element by which the array was partitioned):
```text
[ 6  0  5  2 17  2 10 17  0 13] 
[ 0  0  2  2  5  6 10 13 17 17]
              ^
```
### Indirect partial sort

Just like regular sorting, partial sorting can be performed indirectly.
The function `numpy.argpartition()` creates an indirect partition by the k-th parameter along the given axis.
It returns an **array of indices** of the same shape as the parent array in partitioned order.

```python
x = np.array([8, 3, 4, 2, 1, 7, 0, 10, 5])
print(np.argpartition(x, 4))
print(x[np.argpartition(x, 4)])
```
Output:
```text
[3 6 4 1 2 8 5 7 0]
[ 2  0  1  3  4  5  7 10  8]
              ^
```
In 2-D:
```python
x = np.array([[3, 4, 2, 5, 0], [1, 3, 1, 2, 0]])
index_array = np.argpartition(x, kth=2, axis=-1)
print(np.take_along_axis(x, index_array, axis=-1))  # same as np.partition(x, kth=1)
```
Output:
```text
[[0 2 3 5 4]
 [0 1 1 2 3]]
```
### Task
You have an array `arr` with 20 random numbers and a target value `target`. You need to find `k = 3` data points
in the array `arr` that are the closest to `target` by value. The array `differences` contains the distances
between `target` and each element of `arr`.
1. Get the indices of `distances` partitioned by the k-th element.
2. Rearrange `arr` using those indices and
3. Get only `k` nearest elements to `target`.

<div class="hint">See examples in the task description for 1 and 2. Use slicing for 3.</div>
