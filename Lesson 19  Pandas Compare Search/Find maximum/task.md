## Find Maximum (or Minimum)

There are several ways to find the maximum value in an array. The most straightforward way is to 
use [`numpy.amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html), which
returns the maximum of an array or the maximum along an axis:

```python
a = np.array([[0, 1], [2, 3]])
print(np.amax(a))          # Maximum of the flattened array
print(np.amax(a, axis=0))   # Maxima along the first axis
print(np.amax(a, axis=1))   # Maxima along the second axis
```
Output:
```text
3
[2 3]
[1 3]
```
Sometimes, it might come in handy to know the index of the maximum element. In such a case,
you can use [`numpy.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html),
which returns the indices of the maximum values along an axis:

```python
a = np.array([[10, 11, 12], [13, 14, 15]])
print(np.argmax(a))
print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))
```
Output:
```text
5
[1 1 1]
[2 2]
```
In case you need to perform elementwise comparison between two arrays of equal shape (or broadcastable
to a common shape), [`numpy.maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html) is the function for you.
It compares two arrays and returns a new array containing the elementwise maxima. If the two input
arrays are broadcastable to a common shape, then that shape becomes the shape of the output.

```python
print(np.maximum([100, 0, 7], [99, 5, 2]))
```
Output:
```text
[100   5   7]
```

Functions [`numpy.amin`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin), 
[`numpy.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin), and 
[`numpy.minimum`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum) provide symmetric functionality
for finding minima.

### Task
1. Import data from the file `data.csv` into an array; `dtype` has to be `np.int64`.
2. Find the indices of maximum values in each row.
3. Use these indices to extract the maximum elements from each row and assign the resulting array to the variable `result`.
Please use this exact name.

You can add any `print` statements you like to the `main` block to help you figure out this task.

<div class="hint">
For (3), you will need the function <code>numpy.take_along_axis</code>, which we talked about in the task "Sort".
</div>

<div class="hint">
Note the shape of the index array. To use it with <code>numpy.take_along_axis</code> to extract the maximum elements from
the data, it needs to be reshaped. You could use <code>numpy.reshape</code> and specify the shape you need, or use another function,
<a href="https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html"><code>numpy.expand_dims(a, axis)</code></a>, 
in which case you do not need to specify the desired shape.
</div>
