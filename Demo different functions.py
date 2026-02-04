'''This program demonstrates print(), data types, variables, inputs and f-strings'''
# Print:
# print() is a function that outputs whatever is inside the brackets
# numbers can be included directly in the brackets
print(123)
print(1.5)

# when printing text, it must be in speechmarks which turns it into a string
print("Hello")

# Data types:
# There are lots of different data types:
# Integers - decimals (floating point numbers)
# Text - strings
# Boolean - true or false

# Variables:
# We use variables to store information
# variables must be all lower case
name = "Pluto"
# if you want multiple words in the variables, use underscore
first_name = "John"
last_name = "Smith"
age = 14
# You can include variables inside print() statements
print(name)
# To combine variables with a string, we use f-strings
# The variable goes inside the curly brackets {}
print(f"My dog is called {name} and he is {age} years old")

# We can use input() to get input from the user
user_name = input("What is your name?")
# Print hello to the user
print(f"Hello {user_name}")
# Print hello to the user and ask them how old they are
print(input(f"Hi {user_name}, how old are you?"))