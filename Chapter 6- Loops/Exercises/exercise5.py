# Exercise 5: No Pastrami :ballot_box_with_check:

# listing sandwich orders

sandwich_orders = ["chicken sandwich", "pastrami", "grilled cheese sandwich", 
                   "pastrami", "ham and cheese sandwich ", "pastrami", "tuna sandwich"]

print ("\nSandwich Orders:\n")
for sandwiches in sandwich_orders:
    print(f'{sandwiches}')

# removing pastrami because it ran out

print ("\nSorry! Unfortunately, the Deli has ran out of pastrami.\n")

run_out = "pastrami"

while run_out in sandwich_orders:
    sandwich_orders.remove(run_out)

# making the sandwich orders 

for sandwich in sandwich_orders:
    print (f'I made your {sandwich}!')

# finished sandwiches list

print ("\nFinished sandwiches:\n")
for sandwiches in sandwich_orders:
    print(f'{sandwiches}')