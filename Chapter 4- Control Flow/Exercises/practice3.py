# chap 4 practice 3

"""Write a python program with nested decision structures that perform the following: If amount1
is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2"""

# assigning variables

amount1 = 18
amount2 = 81

# first if condition

if amount1 > 10 and amount2 < 100:

    # second if condition after passing the first 

    if amount1 > amount2:
        print ("Amount 1 is greater than Amount 2.")
    else:
        print ("Amount 2 is greater than Amount 1.")

else:
    print ("Conditions are not met.")
