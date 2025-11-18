

# arr = [1, 2, 3]

# for i in range(len(arr)):
#     current_sum = 0
#     for j in range(i, len(arr)):
#         current_sum += arr[j]
#         print("sum of all arrays", current_sum)


#In how many subarrays index 1 is present

import array as ar

arr = ar.array('i', [1, 2, 3, 4])
print(arr)

# for i,j in enumerate(arr):

sum = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        sum += arr[j]
print("Sum of all subarrays:", sum)

print("--------------------------------------------------")

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

sum = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        sum += arr[j]
print("Sum of all subarrays using numpy array:", sum)

print("--------------------------------------------------")

# in how many subarrays an index 1 will be present

count = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if 1 in arr[i:j+1]:
            count += 1
print("Index 1 is present in", count, "subarrays.")

print("--------------------------------------------------")

# sum of all subarrays using formula

n = len(arr)
sum = (n * (n + 1)) // 2
print("Sum of all subarrays using formula:", sum)

print("--------------------------------------------------")

# sum of all subarrays using prefix sum

prefix_sum = np.zeros(len(arr))
prefix_sum[0] = arr[0]
for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
sum = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if i == 0:
            sum += prefix_sum[j]
        else:
            sum += prefix_sum[j] - prefix_sum[i-1]
print("Sum of all subarrays using prefix sum:", sum)

print("--------------------------------------------------")

# i+1 * (n-i)

n = len(arr)
sum = 0
for i in range(n):
    sum += (i + 1) * (n - i) * arr[i]
print("Sum of all subarrays using formula (-- i+1 * (n-i) --:)", sum)

print("--------------------------------------------------")

# time complexity O(n^2)
n = len(arr)
sum = 0
for i in range(n):
    for j in range(i, n):
        for k in range(i, j + 1):
            sum += arr[k]
print("Sum of all subarrays using O(n^2) approach:", sum)

print("--------------------------------------------------")