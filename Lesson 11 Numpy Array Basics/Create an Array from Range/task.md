## Create an Array from a Range

To create arrays containing sequences of numbers, NumPy provides the [`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html?highlight=arange#numpy.arange) 
function. It is analogous to Python's built-in [`range`](https://docs.python.org/3/library/functions.html#func-range) but returns an array.

```python
a = np.arange(10, 100, 10) # 10 is start, 100 is stop, 10 is step
b = np.arange(0, 5, 0.5)
c = np.arange(10)
print(a)
print(b)
print(c)
```
Output:
```text
[10 20 30 40 50 60 70 80 90]
[0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
[0 1 2 3 4 5 6 7 8 9]
```

Due to finite floating point precision, it is generally not possible to predict
the number of elements obtained when `arange` is used with floating point arguments.
Therefore, in most cases, it is better to use the function [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace), which receives
as an argument the number of elements we want to get rather than the step:

```python
a = np.linspace(0, 2, 9)                   # 9 numbers from 0 to 2
print(a)
```
Output:
```text
[0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]
```
`linspace` returns a specified number of evenly spaced samples over the specified interval.

### Task
Implement the function `array_from_range` that returns an array of integers or floats
from a supplied range. The code in the `main` block should help you figure out what parameters 
to define.