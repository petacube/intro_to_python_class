monty_python = "Monty Python"
print(monty_python)

print(monty_python.lower())    # Print lower-cased version of the string

print(monty_python.upper())

print(monty_python.split(" "))

print("_".join(monty_python.split(" ")))

string = "  Hello, World!  "
print(string.strip())  # Output: Hello, World!

string = "Hello, World!"
new_string = string.replace("World", "Python")
print(new_string)  # Output: Hello, Python!

string = "Hello, World!"
index = string.find("World")
print(index)  # Output: 7

string = "Hello, World! Hello, Python!"
count = string.count("Hello")
print(count)  # Output: 2

string = "Hello, World!"
print(string.startswith("Hello"))  # Output: True
print(string.endswith("Python"))   # Output: False

string = "Hello, World!"
encoded_string = string.encode("utf-8")
print(encoded_string)  # Output: b'Hello, World!'
decoded_string = encoded_string.decode("utf-8")
print(decoded_string)  # Output: Hello, World!

raw_string = r"C:\Users\John\Documents"
print(raw_string)  # Output: C:\Users\John\Documents

str1 = "apple"
str2 = "Apple"

print(str1 == str2)      # Output: False
print(str1 < str2)       # Output: True (based on ASCII values)

from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2024-04-21 12:34:56
