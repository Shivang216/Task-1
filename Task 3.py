# Using maths module for calculations:

a = float(input("Enter a number: "))

def square (a):
    return a ** (1/2)
d = square(a)
print(d)

import math
print(math.log(a))

import math
x = math.sin(a)
print(f"The sine of {a} radians is {x}")




# Calculate factorial using a function:

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n - 1))
d = int(input("Enter a number: "))
print("The factorial of", d, "is", factorial(d))









