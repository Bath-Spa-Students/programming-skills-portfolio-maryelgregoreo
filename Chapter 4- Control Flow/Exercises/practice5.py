# chap 4 practice 5

"""Write a Python program that uses the elif statement to determine the season based on the
month provided as input."""

# input a month

month = int(input("Enter a month (numerical) to know its season:"))

# if-elif-else statements

if month in {3, 4, 5}:
    print ("It's spring!")

elif month in {6, 7, 8}:
    print ("It's summer!")

elif month in {9, 10, 11}:
    print ("It's fall!")

else:
    print ("It's winter!")