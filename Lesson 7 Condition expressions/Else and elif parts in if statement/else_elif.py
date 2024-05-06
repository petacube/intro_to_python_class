x = 28

if x < 0:
    print('x < 0')                     # Executes only if x < 0
elif x == 0:
    print('x is zero')                 # If it's not true that x < 0, check if x == 0
elif x == 1:
    print('x == 1')                    # If it's not true that x < 0 and x != 0, check if x == 1
else:
    print('none of the above is true')

name = "John"

if name == "John":
    print(True)
else:
    print(False)

# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))
