# chap 3 practice 5

"""You have given a Python list. Write a program to find value 20 in the list, and if it is present,
replace it with 200. Only update the first occurrence of an item.
Work with the given list:"""
 

list1 = [5, 10, 15, 20, 25, 50, 20]

# while loop to replace all 20s with 200s

while 20 in list1:
    insert = list1.index(20)
    list1[insert] = 200

# print

print(list1)