rows = 5

for row in range(1, rows + 1):
    # Print leading underscores
    print("_ " * (rows - row), end="")

    # Print first star
    print("*", end="")

    # Print middle spaces for rows 3 to 5
    if row >= 3:
        print(" ", end="")

    # Print remaining stars
    print("* *")
