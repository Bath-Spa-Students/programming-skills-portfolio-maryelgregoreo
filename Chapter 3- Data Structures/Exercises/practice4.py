# chap 3 practice 4

"""Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that
copies the values in numbers to numbers2."""

# make an empty list of numbers_1

numbers_1 = []

# a for loop to insert numbers 1-100 to numbers_1

for i in range (1, 101):
    numbers_1.append(i)

# slicing all elements from numbers_1 to numbers_2

numbers_2 = numbers_1[:]

# print

print(numbers_2)
    
