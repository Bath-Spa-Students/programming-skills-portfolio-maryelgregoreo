## Exercise 2: Movie Tickets: 

# assigning variables to input

prompt = "\nHow old are you? Enter 'quit' when you are finished."

# looping the question

while True:
    age = input(prompt)
    if age == 'quit':
        break
    
    age = int(age)

# if statement

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
