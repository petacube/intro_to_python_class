#1
from functools import reduce
#1 score of the string
s="hello"
asci_val = list(map(lambda x: ord(x), "hello"))
pairs_ascii=zip(asci_val,asci_val[1:])
pairs_diff=map(lambda x: abs(x[0] - x[1]),pairs_ascii)
score=reduce(lambda a,b: a+b,pairs_diff)
print(score)

#2
from functools import cache
#@cache
def fib(k):
        """Compute the kth Fibonacci number."""
        prev, curr = 1, 0  # curr is the first Fibonacci number.
        for _ in range(k - 1):
             prev, curr = curr, prev + curr
        return curr
def iseven(n):
        return n % 2 == 0

def sum_even_fibs(n):
        """Sum the first n even Fibonacci numbers."""
        return sum(filter(iseven, map(fib, range(1, n+1))))

print(sum_even_fibs(5))