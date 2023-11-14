# chap 5 practice 1

"""Use a dictionary to store information about yourself."""

# creating a dictionary

my_info = {
            "First Name": "Maryel", 
            "Last Name": "Gregorio",
            "Age": 18,
            "Birthdate": "October 5, 2005"
          }

# using for loop to go through the dictionary and print

for key, value in my_info.items():
    print (f'{key}: {value}')