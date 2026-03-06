''' This program is for a booking system for the local University's vechile rental system'''
cars = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtrek", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace 2"]
seats = ["2","4","4","4","4","4","7","12","12"]
availibility = ["Available", "Available","Available","Available","Available","Available","Available","Available","Available"]
renter = ["No one","No one","No one","No one","No one","No one","No one","No one","No one"]
print(f"{"Car Type:":19} {"Seat Number:":19} {"Availibility":19} Renter")
loop = True
not_available = "Not available"
import sys
while loop == True:
    for i in range(len(cars)):
        print(f"{i+1}. {cars[i]:20} {seats[i]:15} {availibility[i]:20} {renter[i]}")
    get_selection = True
    print("Enter 0 to quit this program")
    if all(item == not_available for item in availibility):
        print("Sorry all cars are booked for the day")
        sys.exit()
    while get_selection == True:
        not_available = "Not available"
        try:
            rental = int(input("Which number car would you like to book?"))
            if rental < 0 or rental > len(cars):
                print("Please input a number from 0 to 9")
            else:
                get_selection = False
        except ValueError:
            print("Invalid input")
    if rental == 0 :
        print("Thank you, see you later")
        sys.exit()
    elif availibility[rental-1] == "Not available":
        print("Sorry this car has been rented out for the day")
    else:
        availibility[rental-1] = "Not available"
    get_name = True
    while get_name == True:
        name = input("Please enter your name:")
        if name.strip() == "":
            print("Invalid input, please try again")
        else:
            renter[rental-1] = name
            get_name = False