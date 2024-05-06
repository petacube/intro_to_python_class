#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.
import functools

x = lambda a: a + 10
print(x(5))

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))


# lambda vs normal function
def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

Max = lambda a, b: a if (a > b) else b
print(Max(1, 2))

List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)

# lambda wioth filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))

print(adults)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)

animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: animal.upper(), animals))

print(uppered_animals)

from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)

import functools

lis = [1, 3, 5, 6, 2, ]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

def compose1(f,g):
        return lambda x: f(g(x))

# why is is this returning 5?
compose1(lambda x: x+1, lambda x: pow(x,2))(2)
# because 2**2+1 = 4+1 =5

def compose2(f, g):
    """
    
    @param f: function or lambda 
    @param g: function or lambda
    @return: function, that is a composition of these two function
    """"""
        def h(x):
            return f(g(x))
        return h

# why is this returning 61?
compose2(lambda x: x+1, lambda x: x*2)(30)