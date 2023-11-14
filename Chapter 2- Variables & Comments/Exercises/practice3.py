# chap 2 practice 3

"""Write a python program that takes an input 5 from user and then type cast those values to string, int
and float in the separate variables. Print all the variables."""

# entering 5 inputs from the user

input_1 = str(input("Enter any word:"))
input_2 = str(input("Enter any word:"))
input_3 = int(input("Enter any number:"))
input_4 = float(input("Enter any number:"))
input_5 = float(input("Enter any number:"))

# storing inputs into string, integer and float

str_var = str(input_1) + str(input_2)
int_var = int(input_3) + int(input_4)
float_var = float(input_5)

# printing 

print (f' String Variable: {str_var}')
print (f' Integer Variable: {int_var}')
print (f' Float Variable: {float_var}')

