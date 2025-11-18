a=int(input("enter no of rows ="))
for i in range(0,a+1):
    for j in range(a+1-i):
        print("*", end="")
    print()