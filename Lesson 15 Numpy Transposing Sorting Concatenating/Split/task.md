## Split

Splitting is a reverse operation of joining. While joining combines several arrays into a 
single one, splitting breaks one array into several.
Numpy functions [`split()`](https://numpy.org/doc/stable/reference/generated/numpy.split.html) and 
[`array_split()`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html) can do just that.
`split()` splits an array into multiple sub-arrays of **equal size**. It accepts an array and the parameter `indices_or_sections`, 
which is an `int` or a 1D array. If it is an integer, `N`, the array will be divided into `N` equal arrays along the axis. 
If such a split is not possible, an error is raised.
The two functions we've mentioned are very similar, the only difference is that `array_split` allows the parameter `indices_or_sections` 
to be an integer that does not divide the axis equally. For an array of length `l` that should be split into `n` sections, 
it returns `l % n` sub-arrays of size `l//n + 1` and the rest of size `l//n`.

```python
x = np.arange(9)
(print(np.split(x, 3)))
```
Output:
```text
[array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
```
Let's try an `N` for which the array cannot be divided into `N` equal parts:
```python
x = np.arange(9)
(print(np.split(x, 2)))
```
Output:
```text
...
ValueError: array split does not result in an equal division
```
However:
```python
print(np.array_split(x, 4))
```
Output:
```text
[array([0, 1, 2]), array([3, 4]), array([5, 6]), array([7, 8])]
```

You can also use the optional parameter `axis` &mdash; the axis along which 
to split, the default value is `0`. Both methods return a list of sub-arrays which are
views into the original one.

Please refer to the documentation for more details about these methods.

### Task
1. Split the array `x` into three arrays of equal shape (`arr1`, `arr2`, and `arr3`) along the axis `0`.
2. Split the array `y` into three arrays `arr4`, `arr5`, and `arr6`:
```text
1. [[0 1]
    [4 5]
    [8 9]] 
```
```text
2.  [[ 2]
    [ 6]
    [10]] 
```
```text
3. [[ 3]
    [ 7]
    [11]]
```
<div class="hint">You might want to use the axis <code>1</code> in the second case.</div>