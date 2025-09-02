#*_ _ _ __*
#*_ _ _ _*
#*_ _ _*
#*_ _*
#*_*

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):  # i = rows to 1
    middle = "_ " * i         # i underscores
    print("*" + middle + "*")


