
rows = int(input("Enter number of rows: "))
underscores = int(input("Enter number of underscores in the middle: "))

middle = "_ " * underscores 

for i in range(rows):
    print("*" + middle + "*")
