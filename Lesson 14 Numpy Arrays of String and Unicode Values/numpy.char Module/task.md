## `numpy.char` Module

[`numpy.chararray`](https://numpy.org/doc/stable/reference/generated/numpy.chararray.html) used to provide a view of arrays of string and [unicode](https://docs.python.org/3/howto/unicode.html) values.
However, the `chararray` class currently exists only for backwards compatibility, and
it is not recommended for new development. Starting from numpy 1.4, if 
one needs arrays of strings, it is recommended to use arrays of `dtype` [`object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_), 
[`string_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.string_), or [`unicode_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.unicode_), and use the functions in the [`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html) module for 
fast vectorized string operations.

### Bytes

[Bytes](https://docs.python.org/3/library/stdtypes.html#bytes) objects are immutable sequences of single bytes. Since many major binary protocols are based on the ASCII 
text encoding, bytes objects offer several methods that are only valid when working with ASCII compatible data 
and are closely related to string objects in a variety of other ways. The syntax for bytes literals is largely the same as that for string literals, except that a `b` prefix is added:

- Single quotes: `b'still allows embedded "double" quotes'`;

- Double quotes: `b"still allows embedded 'single' quotes"`;

- Triple quoted: `b'''3 single quotes''', b"""3 double quotes"""`.

### `encode` and `decode`

[`numpy.encode`](https://numpy.org/doc/stable/reference/generated/numpy.char.encode.html?highlight=encode) calls [`str.encode`](https://docs.python.org/dev/library/stdtypes.html#str.encode) elementwise. The latter returns an encoded version of the string as a bytes object.

[`numpy.char.decode`](https://numpy.org/doc/stable/reference/generated/numpy.char.decode.html) is used to 
decode the input string based on the [codec](https://docs.python.org/dev/library/codecs.html#module-codecs) specified. 
The set of available codecs is taken from the Python standard library.

```python
x = np.array(['ABCDE', '  fghijklm', 'noPQRST  ', 'UvWxyz'])
print("Input is :", x)
e = np.char.encode(x, encoding='cp500')
print("\nAfter encoding: ", e)
d = np.char.decode(e, encoding='cp500')
print("\nAfter decoding: ", d)
```
Output:
```text
Input is : ['ABCDE' '  fghijklm' 'noPQRST  ' 'UvWxyz']

After encoding:  [b'\xc1\xc2\xc3\xc4\xc5' b'@@\x86\x87\x88\x89\x91\x92\x93\x94'
 b'\x95\x96\xd7\xd8\xd9\xe2\xe3@@' b'\xe4\xa5\xe6\xa7\xa8\xa9']

After decoding:  ['ABCDE' '  fghijklm' 'noPQRST  ' 'UvWxyz']
```

### Task 

At the moment, the function `read_data` returns an array of bytes objects. 
Change the code so that it returns an array of strings. The second `print` statement
has to print `<class 'numpy.str_'>`.


