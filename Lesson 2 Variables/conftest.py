
# conftest.py

import sys
import os

# Add Assignments directory to Python path
folder_list=[
"Arithmetic operators",
"Assignments",
"Boolean operators",
"Comparison operators",
"Type conversion",
"Undefined variable",
"Variable definition",
"Variable types"
]
for f in folder_list:
	sys.path.append(os.path.abspath(f))
print(sys.path)