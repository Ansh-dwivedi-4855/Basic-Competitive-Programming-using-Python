A = [1, 2, 3]
B = 3
result = []

for i in A:
    result.append(i + B)

print(result)



N = int(input())


A = list(map(int, input().split()))


maximum = A[0]
minimum = A[0]

for i in A:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print(maximum, minimum)

