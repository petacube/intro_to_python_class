## Translate

Sometimes, you might need to remove certain characters from your array of strings or replace them with 
some other characters in accordance with some rule or translation table. For that purpose, you can use
[`numpy.char.translate(a, table, deletechars=None)`](https://numpy.org/doc/stable/reference/generated/numpy.char.translate.html), 
where 
- `a` is the input array of `str` or `unicode`; 
- `table` is either a dictionary or a mapping table describing how to perform the replace;
- `deletechars` (optional) is a `str` specifying the characters to be deleted,

It calls [`str.translate`](https://docs.python.org/dev/library/stdtypes.html#str.translate) for each element in `a` and
returns a copy of the string with all characters occurring in the optional argument `deletechars` 
removed and the remaining characters mapped through the given translation table.
It outputs an array of `str` or `unicode`, depending on the input type.

You can use the [`str.maketrans()`](https://docs.python.org/dev/library/stdtypes.html#str.maketrans) method to create a mapping table.
If a character is not specified in the dictionary/table, the character will not be replaced.

Here are some examples:

```python
text = np.array(["Hello,", "my", "dear", "friends!"])
print(np.char.translate(text, str.maketrans("aeiouy", "______")))  # The first two maketrans arguments must have equal length.
```
Output:
```text
['H_ll_,' 'm_' 'd__r' 'fr__nds!']
```
Let's now add the optional `deletechars` parameter:
```python
print(np.char.translate(text, str.maketrans("eyn", "EYN", ',!')))
```
Output:
```text
['HEllo' 'mY' 'dEar' 'friENds']
```
As you can see, in the resulting array, not only were the characters `"eyn"` substituted with `"EYN"`, but 
also the characters `","` and `"!"` were deleted.

You can also use [string constants](https://docs.python.org/dev/library/string.html?highlight=string%20punctuation#string-constants) in place of `deletechars` in case you need to get rid of
all kinds of punctuation, numbers, or other kinds of characters. For example, you can remove
the characters `"0123456789"`:

```python
import string

text = np.array(["ABC123,", "Really??!!", "001_So", "Weird!"])
print(np.char.translate(text, str.maketrans("", "", string.digits)))
```
Output:
```text
['ABC,' 'Really??!!' '_So' 'Weird!']
```
Or, you can remove digits and punctuation (`string.digits` and `string.punctuation`):
```python
print(np.char.translate(text, str.maketrans("", "", string.digits + string.punctuation)))
```
Output:
```text
['ABC' 'Really' 'So' 'Weird']
```

### Task

Implement the function `remove_extra_stuff` so that for the given `text`, the code
would print `"This is almost a normal sentence now"`.

<div class="hint">You will need to replace uppercase vowels with lowercase ones and remove three different kinds
of characters.</div>

<div class="hint">Check out the page describing string constants linked in the
task description to find the ones you can use.</div>

--------------------------------------------------------------------------------

Congratulations on completing the first part of the course! Now you might want 
to move on to the next section to try yourself in solving some problems that are closer to real-life applications.