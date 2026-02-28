''' This program is about barcodes '''
loop = True
while loop == True:
    code = int(input("Enter the barcode:"))
    barcode = len(code)
    if code == 13:
        country = barcode[0:2]
        manufacture = barcode[2:7]
        product = barcode [7:12]
        print(f"Country of origin: {country}")
        print(f"Manufacturer: {manufacture}")
        print(f"Product code: {product}")
        loop = False
    else:
        print("Please enter a valid barcode")