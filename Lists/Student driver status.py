''' This code is about student driving status '''
students = ["Alan", "Brianna", "Charlie", "Dora"]
status = ["No licence", "No licence", "Learners", "Restricted"]
loop = True
while loop == True:
    loop1 = True
    loop2 = True
    for i in range(len(students)):
        print(f"{i+1}. {students[i]:10} {status[i]}")
    while loop1 == True:
        try:
            student = int(input("Select student to update (0 to quit):"))
            loop1 = False
        except ValueError:
            print("Inavild input, please try again")
    if student == 0:
        print("Thank you, see you later")
        loop = False
    elif student > 0 and student <= 4:
        if student == 1:
            while loop2 == True:
                new_status = input(f"What is {students[0]}'s new driver status:")
                if new_status in status[0]:
                    print("Already there")
                    loop2 = False
                elif new_status == "Learners" or new_status == "learners":
                    if new_status == "learners":
                        if "Learners" in status[0]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[0] = "Learners"
                            loop2 = False
                    else:
                        status[0] = new_status
                        loop2 = False
                elif new_status == "No licence" or new_status == "no licence":
                    if new_status == "no licence":
                        if "No licence" in status[0]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[0] = "No licence"
                            loop2 = False
                    else:
                        status[0] = new_status
                        loop2 = False
                elif new_status == "Restricted" or new_status == "restricted":
                    if new_status == "restricted":
                        if "Restricted" in status[0]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[0] = "Restricted"
                            loop2 = False
                    else:
                        status[0] = new_status
                        loop2 = False
                else:
                    print("Invalid input, please try again")
        elif student == 2:
            while loop2 == True:
                new_status = input(f"What is {students[1]}'s new driver status:")
                if new_status in status[1]:
                    print("Already there")
                    loop2 = False
                elif new_status == "Learners" or new_status == "learners":
                    if new_status == "learners":
                        if "Learners" in status[1]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[1] = "Learners"
                            loop2 = False
                    else:
                        status[1] = new_status
                        loop2 = False
                elif new_status == "Restricted" or new_status == "restricted":
                    if new_status == "restricted":
                        if "Restricted" in status[1]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[1] = "Restricted"
                            loop2 = False
                    else:
                        status[1] = new_status
                        loop2 = False
                elif new_status == "No licence" or new_status == "no licence":
                    if new_status == "no licence":
                        if "No licence" in status[1]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[1] = "No licence"
                            loop2 = False
                    else:
                        status[1] = new_status
                        loop2 = False
                else:
                    print("Invalid input, please try again")
        elif student == 3:
            while loop2 == True:
                new_status = input(f"What is {students[2]}'s new driver status:")
                if new_status in status[2]:
                    print("Already there")
                    loop2 = False
                elif new_status == "Learners" or new_status == "learners":
                    if new_status == "learners":
                        if "Learners" in status[2]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[2] = "Learners"
                            loop2 = False
                    else:
                        status[2] = new_status
                        loop2 = False
                elif new_status == "No licence" or new_status == "no licence":
                    if new_status == "no licence":
                        if "No licence" in status[2]:
                            print("Already there")
                        else:
                            status[2] = "No licence"
                            loop2 = False
                    else:
                        status[2] = new_status
                        loop2 = False
                elif new_status == "Restricted" or new_status == "restricted":
                    if new_status == "restricted":
                        if "Restricted" in status[2]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[2] = "Restricted"
                            loop2 = False
                    else:
                        status[2] = new_status
                        loop2 = False
                else:
                    print("Invalid input, please try again")
        else:
            while loop2 == True:
                new_status = input(f"What is {students[3]}'s new driver status:")
                if new_status in status[3]:
                    print("Already there")
                    loop2 = False
                elif new_status == "Learners" or new_status == "learners":
                    if new_status == "learners":
                        if "Learners" in status[3]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[3] = "Learners"
                            loop2 = False
                    else:
                        status[3] = new_status
                        loop2 = False
                elif new_status == "No licence" or new_status == "no licence":
                    if new_status == "no licence":
                        if "No licence" in status[3]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[3] = "No licence"
                            loop2 = False
                    else:
                        status[3] = new_status
                        loop2 = False
                elif new_status == "Restricted" or new_status == "restricted":
                    if new_status == "restricted":
                        if "Restricted" in status[3]:
                            print("Already there")
                            loop2 = False
                        else:
                            status[3] = "Restricted"
                            loop2 = False
                    else:
                        status[3] = new_status
                        loop2 = False
                else:
                    print("Invalid input, please try again")
    else:
        print("Invalid input, please try again")