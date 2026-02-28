'''Demonstrates how a conditional statement (if/else) works
It asks the user for a password and then checks if it is correct'''

# Set password
SAVED_PASSWORD = "carrots"

# Ask for password and store in variable
password = input("Please enter your password:")

# Check if it is correct
if password == SAVED_PASSWORD:
    print("Correct password!")
else:
    print("Incorrect. Get out!")