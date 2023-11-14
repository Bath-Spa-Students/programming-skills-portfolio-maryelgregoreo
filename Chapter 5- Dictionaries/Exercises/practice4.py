# chap 5 practice 4

"""Write a Python program to iterate through both the keys and values of a dictionary and print
them"""

# creating a dictionary

le_sserafim = {
               "Leader": "Kim Chaewon",
               "Oldest": "Miyawaki Sakura",
               "ex-opera": "Huh Yunjin",
               "ex-ballerina": "Nakamura Kazuha",
               "Youngest": "Hong Eunchae"
              }

print ("Members")

# using for loop to iterate through keys and values and printing

for key, value in le_sserafim.items():
    print (f'{key}: {value}')