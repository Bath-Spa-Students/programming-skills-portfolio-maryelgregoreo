# chap 7 practice 3

"""Write a Python program that uses a function to check if a given number is prime or not."""

# inputing in the number variable

number = int(input("Enter a number:"))

# def prime_number

def prime_number (number):
    if number <= 1:
        return False
    
# for loop to find determine if the number is prime or not

    for i in range (2, number):
        if number % i == 0:
            return False
    return True
    
# printing result 

result = prime_number(number)

if result:
    print (f'{number} is a prime number!')
else:
    print (f'{number} is NOT a prime number!')