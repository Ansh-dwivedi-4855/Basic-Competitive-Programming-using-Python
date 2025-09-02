rows = 5

for row in range(1, rows + 1):
    # Leading underscores
    print("_ " * (row - 1), end="")

    # Print stars based on row
    if row == 1:
        print("*   * * * *")
    elif row == 2:
        print("* * * *")
    elif row == 3:
        print("* * *")
    elif row == 4:
        print("*  *")
    else:  # row 5
        print("*")
