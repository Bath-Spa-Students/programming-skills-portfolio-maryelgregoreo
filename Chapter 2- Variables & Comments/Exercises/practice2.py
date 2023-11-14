# chap 2 practice 2

""" Write a python program that takes courses marks as input and then calculates average of all the
courses. After calculating the average, calculate the percentage of a student using total marks. Assume
the total of all the courses marks is 500 or take the total marks from the user as input."""

# enter the needed values for average and percentage

numbers_of_courses = int(input("Enter the amount of your courses:"))

total_marks = int(input("Enter the amount of total marks:")) * (numbers_of_courses)

course_marks = []

# looping to input all marks in all number of courses

for i in range (int(numbers_of_courses)):
    course_marks = int(input(f'Enter your course marks {i + 1}:'))

# inputting your total course marks

total_of_course_marks = int(input("Enter the total of your course marks:"))

# calculating for the average 

average = total_of_course_marks / numbers_of_courses

# calculating for the percentage

percentage = (total_of_course_marks / total_marks ) * 100

# printing the average and perceentage

print(f"Average: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
