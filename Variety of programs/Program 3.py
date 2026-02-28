''' This program asks the user for numbers between 50 and 100. It should keep adding those numbers until the total is larger than 200 '''
NUMBER = 200
total = 0
while total <= 200:
    number = float(input("Please enter a number from 50 to 100:"))
    if number >= 50 and number <= 100:
        total = number+total
        print(f"The total is currently {total}")
    else:
        print("Please input a number from 50 to 100")
