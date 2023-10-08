## Transpose a 1D array

In terms of programming 
languages, it is not possible to transpose a 1D array: the transpose of a 1D array is still a 1D array.

A 1D array is a row of a matrix. If we have to transpose it, we must convert 
this 1D matrix to a 2D matrix and then transpose it. Check out the example below for 
an illustration.

```python
a = np.array([0, 10, 20, 30, 40])
b = np.array([[0, 10, 20, 30, 40]])  # Or: b = a.reshape(1, 5)
print(a)
print(b)
print(a.shape)
print(b.shape)
print(a.T)
print(b.T)
```
Output:
```text
[ 0 10 20 30 40]
[[ 0 10 20 30 40]]
(5,)
(1, 5)
[ 0 10 20 30 40]
[[ 0]
 [10]
 [20]
 [30]
 [40]]
```
The transpose of the 1D array is the same as the array itself, 
but the transpose of the 2D array is something completely different.

### Task
Implement the function `reshape_transpose`, which accepts three parameters:
`start`, `stop`, and `step`, generates a 1D array using `arange`, and returns a transposed array.
