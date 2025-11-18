A = list(map(int, input().split))
B = int(input("Enter the no. "))

Count = 0
for i in A:
    if B==i :
        Count =+ 1
        print(Count)


