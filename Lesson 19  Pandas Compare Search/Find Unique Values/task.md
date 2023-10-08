## Find Unique Values

The [`numpy.unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html) function is pretty 
straightforward – it finds unique elements in the input array and returns them as a sorted array:

```python
print(np.unique([1, 1, 2, 2, 3, 3]))
```
Output:
```text
[1 2 3]
```
Additionally, `numpy.unique` can:

- identify unique rows or columns of an array (when the `axis` parameter is given, when not – search is performed on the **flattened** input array):

```python
a = np.array([[1, 2, 6], [4, 2, 3], [4, 2, 3]])
print(np.unique(a))
print(np.unique(a, axis=0))
```
Output:
```text
[1 2 3 4 6]
[[1 2 6]
 [4 2 3]]
```

- return the unique values and the number of occurrences of each unique value (`return_counts=True`):
```python
a = np.array([1, 2, 6, 4, 2, 3, 2])
print(np.unique(a, return_counts=True))
```
Output:
```text
(array([1, 2, 3, 4, 6]), array([1, 3, 1, 1, 1]))
```

- return the index of the first occurrences of the unique values (`return_index=True`):

```python
a = np.array([1, 2, 6, 4, 2, 3, 2])
unique, index = np.unique(a, return_index=True)
print(unique, index)
```
Output:
```text
[1 2 3 4 6] [0 1 5 3 2]
```
### Task
You are given a dataset in the file `data.csv`. The first column contains ids (class labels),
all other columns – values for some metrics collected for each entry.
1. [Load the dataset](course://NumPy/Array Basics/Reading and Writing Files) from the file into `csv`. Mind the header!
2. [Split](course://NumPy/Array Indexing and Slicing/Indexing Basics) the dataset into `data` (a 2D array) and `labels` (a 1D array of **integers**).
3. Determine the list of classes represented in the dataset (it should be assigned to 
the variable `classes`).
4. Find unique values and their counts in the dataset (`data`).
5. Find the index (in the array from previous step) of the most frequent measurement value (`most_frequent_index`) and get the measurement itself
`most_frequent_measurement` using that index.

<div class="hint">For the last one, you could use <code>numpy.argmax</code>.</div>
