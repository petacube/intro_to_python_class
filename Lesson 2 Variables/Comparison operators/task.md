## Comparison operators

Python has many types of comparison operators, including: 
- `<` less than
  
- `>` greater than 
  
- `==` equal 
  
- `>=` greater or equal
  
- `<=` less or equal
  
- `!=` not equal

The operators  compare the values of two objects. The objects do not need 
to have the same type.


All comparison operations in Python have the same priority, which is lower than
that of any arithmetic, shifting or bitwise operation. Comparisons yield boolean 
values: either `True` or `False`. Comparisons can be chained arbitrarily, and 
expressions like `a < b < c` have the 
conventional mathematical meaning. Read more on comparisons <a href="https://docs.python.org/3/reference/expressions.html#comparisons">here</a>.
### Task
 - Check whether the value of the variable `three` is strictly greater than the value of 
the variable `two`.
 - Check whether the value of the variable `one` is strictly smaller than the value of
   the variable `three`.
 - Check whether the value of the variable `three` is strictly greater than both the value of
   the variable `two` and the value of the variable `one`.
 - Check if the variable `one` is not equal to the variable `two`.
 - Check if the variable `three` equals itself.

<div class='hint'>Use the <code>></code> operator.</div>
<div class='hint'>Use the <code><</code> operator.</div>
<div class='hint'>Use both the <code>></code> and the <code><</code> operators.</div>
<div class='hint'>Use the <code>!=</code> operator.</div>
<div class='hint'>Use the <code>==</code> operator.</div>

Comparison operators are type specific. For instance, some types
have build-in order like `integer`, `float`, `date`,'time` but 'string'
does not have order built-in. Thus, when you compare strings you can't say
if one string is bigger than the other. 

You check if strings are equal or longer or substring of each other.  
