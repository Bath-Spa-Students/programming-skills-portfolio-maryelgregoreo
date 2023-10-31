## Exercise 4: Deli 

# creating a list for 'sandwich_orders' and an empty list for 'finished_sandwiches'

sandwich_orders = ["chicken", "grilled cheese ", "ham and cheese", "tuna"]

finished_sandwiches = []

# looping sandwich orders to finished sandwiches

for sandwich in sandwich_orders:
    print (f'I made your {sandwich} sandwich!')
    finished_sandwiches.append(sandwich)

# printing finished sandwiches

print ("\nFinished sandwiches:\n")
for sandwiches in finished_sandwiches:
    print(f'{sandwiches} sandwich')