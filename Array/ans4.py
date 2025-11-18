
N = int(input("Enter a Number : "))
arr = list(map(int, input().split()))
for i in range(N):
    current_sum = 0
    for j in range(i, N):
        current_sum += arr[j]
        print(current_sum)
