## Basic String Operations in NumPy

There is a number of functions in NumPy that perform string operations on arrays of string and unicode values by calling 
familiar Python string methods. Here are some examples:

- [`numpy.char.lower`](https://numpy.org/doc/stable/reference/generated/numpy.char.lower.html) 
calls [`str.lower`](https://docs.python.org/dev/library/stdtypes.html#str.lower) on each element of 
the input array and returns an array with the elements converted to lowercase. 
- [`numpy.char.capitalize`](https://numpy.org/doc/stable/reference/generated/numpy.char.capitalize.html)
calls [`str.capitalize`](https://docs.python.org/dev/library/stdtypes.html#str.capitalize) and returns 
a copy of the array with only the first character of each element capitalized.
- [`numpy.char.startswith(a, prefix)`](https://numpy.org/doc/stable/reference/generated/numpy.char.startswith.html) 
calls [`str.startswith`](https://docs.python.org/dev/library/stdtypes.html#str.startswith) elementwise
and returns a boolean array which is `True` when the string element in `a` starts with `prefix`, otherwise `False`.
- [`numpy.char.str_len`](https://numpy.org/doc/stable/reference/generated/numpy.char.str_len.html) returns `len(a)` elementwise, the output is an array of integers.
- [`numpy.char.isnumeric`](https://numpy.org/doc/stable/reference/generated/numpy.char.isnumeric.html) calls the Python built-in 
function `isnumeric()` elementwise. For each element, it returns `True` if there are only numeric characters in the element. 
The output is an array of the same shape as input.

You can explore more [string operations](https://numpy.org/doc/stable/reference/routines.char.html) available in the NumPy module.

### Task 

Implement two functions:

- `read_data` should return an array with text lines converted to uppercase.
- `get_line_lengths` should return an array containing the lengths of the input text lines.

<div class="hint">

The opposite of `numpy.char.lower` is [`numpy.char.upper`](https://numpy.org/doc/stable/reference/generated/numpy.char.upper.html).

</div>