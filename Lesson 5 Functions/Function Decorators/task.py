def my_decorator(f):
    print('decorating', f)
    return f

@my_decorator
def my_function(a, b):
    return a + b

print(my_function(1, 2))


# modify parameters
from datetime import datetime

def add_current_time(f):
    def wrapped(*args, **kwargs):
        return f(datetime.utcnow(), *args, **kwargs)
    return wrapped

def test(time, a, b):
    print('I received arguments', a, b, 'at', time)

test = add_current_time(test)

test(1, 2)



# report the parameters
def trace1(fn):
        def wrapped(z):
            print('-> ', fn, '(', z, ')')
            result=fn(z)
            print("Returned " + str(result))
            return result
        return wrapped
@trace1
def triple(x):
        return 3 * x

triple(10)
# this is same as
#trace1(triple(10))