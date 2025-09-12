#This code will calculate the distance between two points on a 2D plane using the Euclidean distance formula.

import math

#Taking values from user
print("Point 1")
x1 = float(input("Enter the x coordinate: "))
y1 = float(input("Enter the y coordinate: "))
print("Point 2")
x2 = float(input("Enter the x coordinate: "))
y2 = float(input("Enter the y coordinate: "))

#Calculating the distance using the Euclidean distance formula
val1 = pow((x2 - x1), 2)
val2 = pow((y2 - y1), 2)
sumval = val1 + val2
distance = math.sqrt(sumval)

print("The distance between the two points is", round(distance, 2) , ".")