## Search

You can search an array for a certain value or for values that satisfy a condition, 
and return the **indices** that get a match.

You can use the [`numpy.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html) method:

```python
a = np.array([0, 10, 4, 11, 7, 3])
print(np.nonzero(a < 5))
print(np.nonzero(a == 7))
print(a < 5)
```
Output:
```text
(array([0, 2, 5]),)
(array([4]),)
[ True False  True False False  True]
```
`numpy.nonzero` returns the indices of the elements that are non-zero.
A common use for it is to find the indices of an array where a condition is 
`True`. For the array `a`, the condition `a < 5` is a boolean array (see the example above). 
`False` is interpreted as `0`, therefore, `np.nonzero(a < 5)` yields the indices of 
`a` where the condition is true. Using the result to index `a` (`a[np.nonzero(a < 5)]`) is equivalent to 
using the mask directly (`a[a < 5]`), and the latter is the preferred spelling.

`np.nonzero(a < 5)` is equivalent to `np.where(a < 5)` (which also returns the indices of elements in the input array where the condition is satisfied):

```python
print(np.where(a < 5))
```
Output:
```text
(array([0, 2, 5]),)
```
However, [`numpy.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html) can also be used in a different way: if provided with a condition
and two input arrays, `numpy.where(condition[, x, y])` returns **elements** (not indices) chosen from 
`x` or `y` depending on the condition:

```python
a = np.array([0, 0, 0, 0, 0, 5, 6, 7, 8, 9])
b = a * 10
print(np.where(a < 5, a, b))
```
Output:
```text
[ 0  0  0  0  0 50 60 70 80 90]
```

In fact, the first argument accepted by this function is also an array – a boolean array, `a < 5` in this case.
Therefore, it can also be used like this:

```python
result = np.where([False, True, False], [1, 1, 1], [7, 8, 9])
print(result)
```
Output:
```text
[7 1 9]
```
`x`, `y`, and `condition` arrays need to be broadcastable to some shape.

### Task

You are given an array of random integers between 0 and 25 representing temperatures registered on
certain days of the week. Using the functionality you've just learned about, generate an array `result`, 
which contains strings, either `Low` or `High`, in an order depending on whether the corresponding day of the 
week was warmer than 15 degrees (`High`) or not (`Low`). You will probably need to define two additional arrays, `high` and `low`, 
containing strings that will be used for `result`.

In addition, `warm_days` should contain the names of the warm days (with temperatures above 15).

<div class="hint"><code>result</code> should look something like <code>['High' 'Low' 'Low' 'Low' 'High' 'High' 'High']</code>.</div>

<div class="hint">Use <code>numpy.where</code> with a condition about temperatures and two input arrays <code>high</code> and <code>low</code> to get the <code>result</code>.</div>

<div class="hint">For the last part, use <code>numpy.nonzero</code> or a direct mask.</div>