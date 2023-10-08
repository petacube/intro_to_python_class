## bincount

A use case somewhat related to finding unique values is counting the number of occurrences of each value in an array.
[`numpy.bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html) is the function that does just that for an array of non-negative ints. It returns 
the result of binning the input array, which is the count of how many times every integer on the interval from 0 
to the maximum value in the input array is encountered in the input array.
Therefore, the number of bins (of size 1) is one larger than the largest value in the input array. 

```python
a = np.array([1, 1, 1, 2, 3, 7, 7])
print(np.bincount(a))
```
Output:
```text
[0 3 1 1 0 0 0 2]
```
[`numpy.histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html) is somewhat similar, but it allows for variable bin size. 
You can specify the number of bins (`bins=10` by default) and `range`, which is `(a.min(), a.max())` by default. 
The function returns two arrays: the values of the histogram and the bin edges.
It can also return the value of the probability density function at each bin (normalized such that the integral over the range is 1) instead 
of the number of samples in the bin if you use the `density=True` argument.

Using the array `a` we defined earlier, we get:
```python
bincounts = np.bincount(a)
hist, _ = np.histogram(a, range=(0, a.max()), bins=a.max() + 1)
print(np.array_equal(hist, bincounts))
```
Output:
```python
True
```
If the input array is multidimensional, the histogram is computed over the flattened array.

### Task

Using some of the functions you've learned in this and in previous tasks, find the most frequent class in the data.

<div class="hint">It might be helpful to use <code>np.bincount</code> on class labels.</div>
<div class="hint">When you've got the binned array, the only thing left to do is get the most populous class using one of the 
functions for finding maxima that we discussed earlier.</div>