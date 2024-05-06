for i in range(5):    # For each number i in range 0-4. range(5) function returns list [0, 1, 2, 3, 4]
    print(i)          # This line is executed 5 times. First time i equals 0, then 1, ...


primes = [2, 3, 5, 7]   # Create new list

for prime in primes:
    print(prime)

# Program to display the Fibonacci sequence up to n-th term
#
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1