'''Demonstrates how a conditional statement (if/else) works
It asks the user for a password and then checks if it is correct'''

# Ask for password and store in variable
password = input("Please enter your password:")

# Check if it is correct
if password == "carrots":
    print("Correct password!")
else:
    print("Incorrect. Get out!")