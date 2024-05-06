# here we will cover higher order functions
# map, filter, reduce, zip,
from functools import reduce

my_list=[1,5,3,10]
result=list(map(lambda x: x+1, my_list))
print(result)

result=list(filter(lambda x: x>=5, my_list))
print(result)

result=reduce(lambda x,y: x+y, my_list)
print(result)

z=list(zip(my_list,my_list[1:]))
print(z)