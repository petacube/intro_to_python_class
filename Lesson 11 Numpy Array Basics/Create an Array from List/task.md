## Create an Array

There are several ways you can create arrays.

First, you can create an array from a regular Python list or tuple using the `array` function. 
The type of the resulting array will be deduced from the type of the elements in the source sequences.

```python
import numpy as np

a = np.array([0, 1, 2])
b = np.array([0.0, 0.1, 0.2])

print(a.dtype)
print(b.dtype)
```
Output:
```text
int64
float64
```

`array` transforms sequences of sequences into two-dimensional arrays, sequences of sequences of 
sequences into three-dimensional arrays, and so on.

```python
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
```
Output:
```text
[[1.5 2.  3. ]
 [4.  5.  6. ]]
```

### Task
Complete the implementation of the function `create_array()` so that it creates an array from a nested list
with specified dimensions.