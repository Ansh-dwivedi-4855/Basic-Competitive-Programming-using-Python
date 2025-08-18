#check whether the last digit is divisibly by 4

num = int(input("Enter a number: "))

if num % 10 == 4:   # last digit nikalne ke liye %10 use karte hain
    print("Last digit is 4")
else:
    print("Last digit is not 4")
