# Exercise 6: Shrinking Guest List :ballot_box_with_check:

# Inviting to dinner

guests = ["Chaewon", "Yunjin", "Kazuha"]

print(f'Hey! Can I take you out to dinner, {guests [0]}?')
print(f'{guests [1]}! Want to go to dinner with me?')
print(f'{guests [2]}, Would you like to go to dinner with me?')

print(f'Oh! {guests [0]} cannot make it to dinner, she is sick.. Let us invite Sakura instead!')


# Chaewon can't make it so let's invite Sakura

guests [0] = "Sakura"

print(f'Hey {guests [0]}! Chaewon cannot make it to dinner, would you like to come instead?')


# There is not enough space at the dinner table

print("Sorry! I can only invite two people for dinner.")

print(f'Hey {guests [0]}, I am sorry but only two people can fit in the table.')
guests.pop(0)

# Invite two people only

print(f'{guests [0]}! Do you still want to go to dinner with me?')
print(f'{guests [1]}, Would you still like to go to dinner with me?')

# the final guest list

print(guests)
