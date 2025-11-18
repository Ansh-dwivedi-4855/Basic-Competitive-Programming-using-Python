

A = list(map(int, input().split()))

maximum = A[0]
minimum = A[0]

for i in A:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print(maximum, minimum)