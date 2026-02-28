''' This program asks the user for two numbers the second numbeer must be bigger than the first. Then the program prints out the two numbers '''
loop = True
while loop == True:
    try:
        number = int(input("Enter a positive number:"))
        number2 = int(input("Enter a positive number that is bigger than the first number:"))
        loop = False
    except ValueError:
         print("Please input a number bigger than 0 and have the second number bigger than the first")
loop = True
while loop == True:
    try:
        if number2 > number:
            print(f"Your two numbers are {number} and {number2}")
            loop = False
        else:
            print("Please have a number bigger than the first")
    except ValueError:
        print("Please input a number bigger than 0 and have the second number bigger than the first")