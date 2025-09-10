#This code asks the user to input three decimal values and calculates the sum of these decimals.

deci1 = float(input("Enter the first number: "))
deci2 = float(input("Enter the secnd number: "))
deci3 = float(input("Enter the third number: "))

sum = deci1+deci2+deci3
newsum = round(sum,2)

print("The total of the three numbers is", newsum , ".")