## Assignments

An augmented assignment is a single statement combining a binary operation and an 
assignment statement, such as `+=`, `-=`, etc.  

An augmented assignment expression like `x += 1` can be rewritten as `x = x + 1` to achieve a similar effect.
You can read more about this <a href="https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements">here</a>.
### Task
Use an augmented assignment to add `5` to `number` and update the variable.  

<div class='hint'>Use the <code>+=</code> operator.</div>

Assignment can be immediate or delayed. For instance 
`x=1` is an immediate assignment. 
But in high-performance libraries, 
which we will cover later in the course distributed libraries like `dask`, `Spark`, `polars` 
assignments are delayed. This delayed assignment is done so library can optimize the series of assignments 
and possibly do them in different order. For example
let say you have series of assignments like this
```python

x=1
y=2
z=3
```
these operators are totally indepedent and can be executed by computer in parallel.
compare that to

```python
x=1
y=x+1
z=y+2
```
these operations cannot be executed in parallel because they depend on each other




