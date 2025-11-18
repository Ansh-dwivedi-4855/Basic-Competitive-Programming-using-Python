
n= int(input("enter a Number :"))
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i, n):
        subarray = arr[i:j+1]
        print(*subarray)
