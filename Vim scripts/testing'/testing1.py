import math

octnum = input("Please enter a number you wish to convert to an octal number. ")
binnum = input("Please enter a number you wish to convert to binary. ")

if octnum.isdigit():
    print(oct(octnum))
else:
    print("That is not a number")
if binnum.isdigit():
    print(bin(binnum))
else:
    print("That is not a number.")

