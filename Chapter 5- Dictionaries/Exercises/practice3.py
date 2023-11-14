# chap 5 practice 3

"""Write a Python program to iterate through the values of a dictionary and print them."""

# creating a dictionary

le_sserafim = {
               "Leader": "Kim Chaewon",
               "Oldest": "Miyawaki Sakura",
               "ex-opera": "Huh Yunjin",
               "ex-ballerina": "Nakamura Kazuha",
               "Youngest": "Hong Eunchae"
              }

print ("Members:")

# iterating through the dictionary using key and printing
for key, value in le_sserafim.items():
    print (value)

