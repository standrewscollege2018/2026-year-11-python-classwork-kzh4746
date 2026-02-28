''' This program is going to create a random game '''
print("In this game you are to pick a number from 1 to 100 and the computer will guess your number. You are to tell the computer hot if it is within 5 numbers away, but if it's further away then that say cold. If the guess is right then say Yes.")
while True:
    number = int(input("Pick a number from 1 to 100:"))
    if number >= 1 and number <= 100:
        break
    else:
        print("Please input a real number.")
for i in range (1,101):
    guess = input(f"Is it {i}?")
    if guess == "Cold":
        for i in range (10,101):
            guess1 = input(f"Is it {i}?")
            if guess1 == "Cold":
                for i in range (15,101):
                    guess2 = input(f"Is it {i}?")
            elif guess1 == "Hot":
                    print("I am close")
            else:
                    print("Invalid input: please input Hot or Cold")
                    if guess2 == "Cold":
                         for i in range (20,101)
    if guess == "Hot":
        print("I am close")
    elif guess == "Yes":
        print("Yes, l got it right")
    else:
        print("Invalid input: please input Hot or Cold")