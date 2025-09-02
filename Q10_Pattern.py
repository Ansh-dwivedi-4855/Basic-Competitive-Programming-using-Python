rows = 5
spaces = 21   

for i in range(1, rows + 1):
    # Left stars
    print("*" * i, end="")

    # Middle spaces
    if i != rows:   
        print(" " * spaces, end="")

    # Right stars
    print("*" * i)

    spaces -= ( (21) // (rows - 1) )
