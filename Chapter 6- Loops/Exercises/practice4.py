# chap 6 practice 4

"""Write a Python program that uses the break statement to exit a for loop when a specific
condition is met."""

# assinging msg variable

msg = "Hello World!"

# for loop that when it prints for 18th time, it breaks

for number in range(50):
    if number > 18:
        break
    print(msg)
    