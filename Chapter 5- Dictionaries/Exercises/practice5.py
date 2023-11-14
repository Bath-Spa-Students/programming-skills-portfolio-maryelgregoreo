# chap 5 practice 5

"""Write a Python program to merge two dictionaries into one."""

# creating two dictionaries

member_1 = {
            "First Name": "Chaewon",
            "Last Name": "Kim",
            "Birthdate": "August 1, 2000",
            "Age": 23,
            "Animal Representation": "Baby Cheetah"
            }

member_2 = {
            "First Name": "Sakura",
            "Last Name": "Miyawaki",
            "Birthdate": "March 19, 1998",
            "Age": 25,
            "Animal Representation": "Cat"
            }
print ("Members:")

# using for loop to combine and organize two dictionaries

for (key1, value1), (key2, value2) in zip (member_1.items(), member_2.items()):
    print (f'{key1}: {value1} \t \  {key2}: {value2}')








