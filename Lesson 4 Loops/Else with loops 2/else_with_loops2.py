def contains_even_number(lst):
    for i in lst:
        if i % 2 == 0:
            print(f"List {lst} contains an even number.")
            break
    else:
        print(f"List {lst} does not contain an even number.")


contains_even_number([1, 9, 8])
contains_even_number([1, 3, 5])

# check if a prime prime number
#A positive integer greater than 1 which has no other factors except
#1 and the number itself is called a prime number. 2, 3, 5, 7 etc. are prime
#numbers as they do not have any other factors.
#But 6 is not prime (it is composite) since, 2 x 3 = 6.
num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")