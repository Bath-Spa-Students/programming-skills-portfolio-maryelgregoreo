# chap 5 practice 2

"""Write a Python program to iterate through the keys of a dictionary and print them"""

# creating a dictionary

le_sserafim = {
               "Leader": "Kim Chaewon",
               "Oldest": "Miyawaki Sakura",
               "ex-opera": "Huh Yunjin",
               "ex-ballerina": "Nakamura Kazuha",
               "Youngest": "Hong Eunchae"
              }

# iterating through the dictionary using key and printing

for key, value in le_sserafim.items():
    print (key)
    