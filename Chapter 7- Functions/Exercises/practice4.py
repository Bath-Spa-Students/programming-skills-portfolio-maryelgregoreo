# chap 7 practice 4

"""Write a Python program that defines a function to calculate the area of a circle, and then
calls that function with a given radius."""

# importing pi

from math import pi

# inputting radius

radius = int(input("Enter radius:"))

# def circle_area and area formula

def circle_area (radius):
    return pi * radius ** 2

# printing

area = circle_area (radius)

print (f'Area of the circle: {area:.2f} sq. units.')
