name = "John"
age = 17

if name == "John" or age == 17:   # Check that name is "John" or age is 17. If so print next 2 lines.
    print("name is John")
    print("John is 17 years old")

tasks = ["Common File Formats", "task2"]    # Create new list

if len(tasks) != 0:
    print("Not an empty list!")

tasks.clear()  # Empty the list

if len(tasks) == 0:
    print('Now empty!')
