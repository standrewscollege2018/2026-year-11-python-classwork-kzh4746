'''This program checks if can donate blood'''

AGE = 16
WEIGHT = 50
age = int(input("Enter your age:"))
weight = int(input("Enter your weight (in kgs):"))
if age >= AGE and weight >= 50:
    print("You are eligible")
else:
    print("You are not eligible")