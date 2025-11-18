n=int(input("enter the number = "))
for i in range(n,n-1):
    for j in range(n-i):
        print("*",end="")
    print()