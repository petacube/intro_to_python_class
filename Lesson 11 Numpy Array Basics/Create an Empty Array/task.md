## Create an Empty Array

Sometimes, the size of an array is known, while its elements are originally unknown. 
NumPy offers several functions to create arrays with initial placeholder content:

- the function [`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros) creates an array full of zeros;
- the function [`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html?highlight=ones#numpy.ones) creates an array full of ones;
- the function [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty) creates an array where the initial content is random and 
depends on the state of the memory.

<details>

By default, the `dtype` of an array created in such a way is [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=float64#numpy.float64), 
but it can be specified otherwise with the keyword argument `dtype`.
</details>

```python
a = np.zeros((3, 4))
b = np.ones((2, 3), dtype=np.int16)
c = np.empty((2, 3))

print(a)
print(b)
print(c)
```
Output:
```text
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[1 1 1]
 [1 1 1]]
[[2.31584178e+077 2.31584178e+077 1.97626258e-323]
 [3.95252517e-323 1.18575755e-322 3.95252517e-323]]
```

Another function, [`full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full), 
returns a new array of a given shape and type filled with a specified value.

```python
a = np.full((2, 2), 10)
print(a)
```
Output:
```text
[[10, 10],
 [10, 10]]
```

### Task
Complete the implementation of the function `create_arrays()` to create arrays `a` and `b`, where:
- array `a` contains only the values `1` of `dtype` `int64` (or `int`);
- array `b` contains only the values `True`.
Both of the arrays should have the shape of `(x,y)`.

<div class="hint">For <code>a</code>, use the function <code>numpy.ones</code>.</div>
<div class="hint">For <code>b</code>, use the function <code>numpy.full</code>.</div>