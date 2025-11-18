# # given an array A of N non-negative numbers and a non-negative number B . kon kon si esi subarrayhain jinka sum 10 se kam hain

# #Input 1
# A = [2,5,6]
# B = 10
# # input 2
# A = [1,11,2,3,15]
# B = 10

# A = [2, 5, 1, 3]
# B = 10

# n = len(A)
# result = []

# for i in range(n):
#     current_sum = 0
#     for j in range(i, n):
#         current_sum += A[j]
#         if current_sum < B:
#             result.append(A[i:j+1])
#         else:
#             break  
# print("Subarrays जिनका sum <", B, "है:")
# for sub in result:
# #     print(sub)

# A = [2, 5, 1, 3]
# B = 10

# n = len(A)
# count = 0

# for i in range(n):
#     current_sum = 0
#     for j in range(i, n):
#         current_sum += A[j]
#         if current_sum < B:
#             count += 1
#         else:
#             break   # आगे sum और बढ़ेगा

# print("Total subarrays जिनका sum <", B, "है:", count)


# count = 0 
# for i in range(0,N):

A = [2, 5, 1, 3]
B = 10

n = len(A)
less_count = 0     # sum < B
equal_count = 0    # sum == B

for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += A[j]
        if current_sum < B:
            less_count += 1
        elif current_sum == B:
            equal_count += 1
        else:
            break   # आगे sum बढ़ेगा, non-negative numbers हैं

print("Subarrays count is", less_count)
print("Subarrays जिनका sum =", B, "है:", equal_count)

