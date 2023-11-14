# chap 6 practice 5

"""Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop."""

# assigning largest_number variable

largest_number = 0

# while loop and integer input

while True:
    user_input = int(input("Enter a number (enter '0' to exit):"))
    number = int(user_input)

# if condition to break

    if user_input == 0:
        break

# if condition to assign the largest number input to largest_number

    if largest_number == 0 or number > largest_number:
        largest_number = number

# print

print (f'Largest Number: {largest_number}')
