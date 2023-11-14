# chap 7 practice 2

"""Write a Python function that calculates the factorial of a given positive integer using
recursion."""

# x as the variable for the number

x = int(input("Enter any number:"))

# def of factorial

def factorial (x):

# if and else condition 

    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial (x-1)
    
# variable for the factorial

result = factorial(x)

# print

print (f' Factorial of {x}: {result}')

