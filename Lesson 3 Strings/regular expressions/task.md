
Regular Expressions with re Module
Regular expressions (regex) are powerful tools for pattern matching and text manipulation. 
Python provides the re module for working with regular expressions.


A regular expression is a sequence of characters that defines a search pattern. It can be used to search, edit, and manipulate text.

Basic Patterns
.: Matches any character except a newline.
^: Matches the start of a string.
$: Matches the end of a string.
*: Matches 0 or more repetitions of the preceding element.
+: Matches 1 or more repetitions of the preceding element.
?: Matches 0 or 1 repetition of the preceding element.
{m}: Matches exactly m repetitions of the preceding element.
{m,n}: Matches between m and n repetitions of the preceding element.
[...]: Matches any single character in the brackets.
[^...]: Matches any single character not in the brackets.
|: Matches either the expression before or after the |.
Using re Module in Python