
A = input("Enter numbers separated by space: ").split()

A = [int(num) for num in A]

total_sum = 0
for num in A:
    total_sum += num

print("Sum of all elements:", total_sum)

