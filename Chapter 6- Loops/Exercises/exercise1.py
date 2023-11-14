## Exercise 1: Pizza Toppings :ballot_box_with_check:

"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you'll add that topping to their pizza."""

# inputting pizza toppings 

pizza_toppings = []

while True:
    toppings = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if toppings.lower() == 'quit':
        break  
    
    pizza_toppings.append(toppings)
    print(f"Adding {toppings} to your pizza.")


# displaying the final list of pizza toppings

if pizza_toppings:
    print("Toppings for your pizzas:")
    for topping in pizza_toppings:
        print(topping)
else:
    print("You didn't choose any toppings for your pizza.")
