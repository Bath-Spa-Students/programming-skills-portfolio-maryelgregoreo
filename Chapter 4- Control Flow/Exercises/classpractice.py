#if and else statement

sales = float (input ("Enter sales:"))
bonus = 0
if sales > 5000:
    bonus = 500
else:
    bonus = 0

print ("Your bonus:" + str(bonus))


#if elif else statement

age = int(input("How old are you?"))

if age >= 22:
    print("You are an adult and should be working!")

elif age >= 18:
    print("You are in college!")

elif age >= 15:
    print("You are in high school!")

elif age >= 13:
    print ("You are in middle school!")

elif age >= 6:
    print("You are in elementary school!")

else:
    print("You are in kindergarten!")