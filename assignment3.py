# assignment 3
# problem 1

def factorial(n):
    if(n<2):
        return 1
    else:
        return n * (factorial(n-1))
f = factorial(5)
print (f)

# problem 2 

import math

a = int( input("insert first no. "))

print(math.sqrt(a))
print(math.log(a))
print(math.radians(a))
