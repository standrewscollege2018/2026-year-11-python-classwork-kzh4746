''' Error catching to prevent invalid data types '''
get_num = True
while get_num == True:
    try:   
        number = int(input("Enter a number:"))
        get_num = False
    except ValueError:
        print("That's not a number")
print(f"You entered {number}")