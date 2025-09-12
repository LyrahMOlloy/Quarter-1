
#This code will calculate the area of a circle based on the radius the user will input.

import math

radius = float(input("Enter the radius of the circle: "))
radius_squared = pow(radius,2)
area = math.pi * radius_squared
final_area = round(area, 2)


print("The area of your circle is ", final_area , "square units.")
