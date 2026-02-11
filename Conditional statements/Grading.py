'''This program calculates the grade based on their marks'''
MIN_A = 90
MIN_B = 70
MIN_C = 50
mark = int(input("Please enter your mark from 0 to 100:"))
if mark >= 0 and mark <= 100:
    if mark >= MIN_A:
        print("Grade: A")
    elif mark >= MIN_B:
        print("Grade: B")
    elif mark >= MIN_C:
        print("Grade: C")
    else:
        print("Grade: Fail")
else:
    print("Invalid mark. It must be between 0 and 100")