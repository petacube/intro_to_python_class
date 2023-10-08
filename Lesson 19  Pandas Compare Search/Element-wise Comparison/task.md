## Elementwise Comparison

Elementwise comparison is when you compare each element of one array to an element of another array.
[`numpy.equal`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html) is a function that returns `(x1 == x2)` elementwise.
It accepts two input arrays which must either have equal `shape` or be broadcastable to a common shape 
(which becomes the shape of the output). Elements of the output array are typically boolean values.

Example:
```python
print(np.equal([0, 1, 3], np.arange(3)))
```
Output:
```text
[ True,  True, False]
```
What is compared are values, not types. So, an int (1) and an array of length one can evaluate as `True`:
```python
print(np.equal(1, np.ones(1)))
```
Output:
```text
[ True]
```
The `==` operator can be used as a shorthand for `np.equal` on ndarrays.

### `numpy.array_equal`

[`numpy.array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html) is a
function that returns `True` if two input arrays have **the same shape and elements** and `False` otherwise.

Examples:
```python
print(np.array_equal([1, 2], [1, 2]))
print(np.array_equal(np.array([1, 2]), np.array([1, 2])))
print(np.array_equal([1, 2], [1, 2, 3]))
print(np.array_equal([1, 2], [1, 4]))
```
Output:
```text
True
True
False
False
```

### Task
Define a **1D** array `b` such that by comparing it elementwise with the array `a`, you can 
get the array `compare_a_b`, which is `array_equal` (has the same elements and shape) to the array in the last
`print` statement. When you run the script, the last `print` statement has to print `True`.

<div class="hint">The array <code>b</code> should be of shape <code>(5,)</code>. Use
<code>np.arange</code> with <code>start</code>, <code>stop</code>, and <code>step</code> arguments.
By looking at the resulting boolean array, you can figure out which integer has to be in 
what position in <code>b</code> and then come up with suitable arguments for the <code>np.arange</code>
function.</div>

<div class="hint">To get the array <code>compare_a_b</code>, use the <code>np.equal</code> function.</div>
