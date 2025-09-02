rows = 5

for i in range(rows):
    # Left stars
    print("*" * (rows - i), end="")

    # Middle spaces
    print(" " * (i * 4), end="")

    # Right stars
    print("*" * (rows - i))
