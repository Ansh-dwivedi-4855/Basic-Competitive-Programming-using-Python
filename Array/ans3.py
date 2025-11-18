
N = int(input("Enter a Number : "))
arr = list(map(int, input().split()))
L = map(int, input().split())
R = map(int, input().split())
L -= 1
R -= 1
result = sum(arr[L:R+1])
print(result)
