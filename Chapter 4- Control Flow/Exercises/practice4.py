# chap 4 practice 4

"""Write a python program with an if-else statement that displays Speed is normal if the speed
variable is within the range of 24 to 56. If the speed variable's value is outside this range, display
'Speed is abnormal"""

# assigning speed and speed range variables

speed = 81
speed_range = range(24, 56)

# if-else statement 

if speed in speed_range:
    print ("Speed is normal.")
else:
    print ("Speed is abnormal.")
