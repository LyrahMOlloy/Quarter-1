name = str(input("Enter your full name in this format (seperated by commas, two first names maximum): First Name, Middle Name, Last Name "))

First_Name, Middle_Name, Last_Name = name.split(",")
wordCount = len(First_Name.split())

if wordCount == 2:
    firstFirst_Name, secondFirst_Name = First_Name.split()
    finFirst_Name = (firstFirst_Name.capitalize())+" "+(secondFirst_Name.capitalize())+","
    finLast_Name = (Last_Name.capitalize())+","
    notMiddle_Name = Middle_Name.capitalize()
    finMiddle_Name = (notMiddle_Name[0])+"."
    print("Formatted Name:",finLast_Name, finFirst_Name, finMiddle_Name) 
else:
    finFirst_Name = (First_Name.capitalize())+","
    finLast_Name = (Last_Name.capitalize())+","
    notMiddle_Name = Middle_Name.capitalize()
    finMiddle_Name = (notMiddle_Name[0])+"."
    print("Formatted Name:",finLast_Name, finFirst_Name, finMiddle_Name) 