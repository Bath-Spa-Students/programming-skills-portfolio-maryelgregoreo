# chap 3 practice 1

"""Given a Python list, write a program to remove all occurrences of item 20.
Given list:"""

list1 = [5, 20, 15, 20, 25, 50, 20]

# make a while loop to remove 20

while 20 in list1:
    list1.remove(20)

# print

print(f'List 1: {list1}')