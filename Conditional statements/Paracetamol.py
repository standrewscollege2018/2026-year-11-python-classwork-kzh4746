'''This program gives recomendation on how much paracetamol you should take'''
AGE = 12
while True:
    age = int(input("What is the patient's age in years? "))
    weight = float(input("What is the patient's weight in kilograms? "))
    if age > 0 and age <= 100:
        if weight > 3:
           break
    else:
        print("Please input a valid number")
if age < 12:
    paracetamol = 10*weight
    print(f"We recommend {paracetamol}mg paracetamol")
else:
    print("We recommend two 500mg tablets")