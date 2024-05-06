def sum_naturals(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total

def sum_cubes(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + pow(k, 3), k + 1
        return total

def sum_for_squares(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + pow(k,2), k+1
        return total

# generalize above functions
def summation(n, term, next):
        total, k = 0, 1
        while k <= n:
            total, k = total + term(k), next(k)
        return total

def natural_summation(n):
    return summation(n=n,term=lambda y: y, next=lambda y: y+1)

def cube_sum(n):
    return summation(n=n,term=lambda y: pow(y,3), next=lambda y: y+1)

def square_sum(n):
    return summation(n=n,term=lambda y: pow(y,2), next=lambda y: y+1)

print(natural_summation(5))
print(cube_sum(3))
print(square_sum(3))

