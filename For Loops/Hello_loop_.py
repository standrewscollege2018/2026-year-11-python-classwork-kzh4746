''' This program asks the user for their name and then prints out hello and then the name three times'''
ranges = int(input("How many names do you wish to enter?"))
for i in range(0,ranges):
    name = input("Enter a name:")
    print(f"Hello {name}")