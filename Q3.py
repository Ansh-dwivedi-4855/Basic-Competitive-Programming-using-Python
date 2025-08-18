# WAP to check if the number is divisible by 3 and the last digit is 4. 
num = int(input("Enter a number: "))

if (num % 3 == 0) and (num % 10 == 4):
    print(f"{num} is divisible by 3 and last digit is 4")
else:
    print(f"{num} does not satisfy both conditions")
