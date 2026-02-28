''' This program will ask the user for two numbers and will then giva a message telling them the two numbers they entered, the larger of their two numbers, and the total of the two numbers'''
loop = True
while loop == True:
    try:
        Number = int(input("Enter a positive number:"))
        Number2 = int(input("Enter another positive number:"))
        loop = False
    except ValueError:
        print("Please input a positive non-decimal number")
print(f"Your two numbers are {Number} and {Number2}")
if Number > Number2:       
    print(f"The bigger number out of the two numbers is {Number}")
elif Number < Number2:
    print(f"The bigger number out of the two numbers is {Number2}")
else:
    print("The two numbers are the same")
Total = Number+Number2
print(f"The sum of the two numbers is {Total}")
loop = False