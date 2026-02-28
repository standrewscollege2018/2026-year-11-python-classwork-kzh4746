''' This program sets a number and lets the user to guess the number '''
import random
NUMBER = random.randint(1,10)
Counter = 0
ask_guess = True
while ask_guess == True:
    guess = float(input("Guess a number between 1 and 10 (number isn't a decimal):"))
    Counter = Counter + 1
    if guess == NUMBER:
        print("That's right!")
        ask_guess = False
    elif guess < NUMBER:
        print("Too low")
    elif guess > NUMBER:
        print("Too high")
    else:
        print("Nope that's wrong. Guess again.")
print(f"Good job it took you {Counter} guesses!")