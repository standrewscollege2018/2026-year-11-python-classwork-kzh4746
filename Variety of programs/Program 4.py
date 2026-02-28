''' This program is about barcodes '''
loop = True
while loop == True:
    barcode = int(input("Please enter the barcode number:"))
    barcode = len(str(barcode))
    if barcode != 13:
        print("This barcode is invalid as it doesn't have 13 numbers")
    else:
        first_digit = barcode[0:1]
        first_two_digit = barcode[0:2]
        first_three_digit = barcode[0:3]
        if first_digit == 0:
            print("This barcode is from USA or Canda")
        elif first_two_digit == 1:
            print("This barcode is from USA")
        elif first_two_digit == 45:
            print("This barcode is from Japan")
        elif first_three_digit == 46:
            print("This barcode is from Russia")
        elif first_three_digit == 380:
            print("This barcode is from Bulgaria")
        elif first_three_digit == 383:
            print("This barcode is from Slovenia")
        elif first_three_digit == 385:
            print("This barcode is from Croatia")
        elif first_three_digit == 389:
            print("This barcode is from Montenegro")
        elif first_three_digit == 390:
            print("This barcode is from Kosovo")