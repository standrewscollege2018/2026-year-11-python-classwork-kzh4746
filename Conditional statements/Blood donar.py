'''This program checks if eligible donate blood'''

MIN_AGE = 16
MIN_WEIGHT = 50
age = int(input("Enter your age (in years):"))
# Using float as users might enter decimals for their weight
weight = float(input("Enter your weight (in kgs):"))
if age >= MIN_AGE and weight >= MIN_WEIGHT:
    print("You are eligible")
else:
    print("You are not eligible")