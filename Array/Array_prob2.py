# # Given an array of integers A , a subarray of an array is said to be good if iy fulfils any one of the criteria :
 
# 1 . lenght of  the subaarray is to be even , 
# and the sum of all elements of the subarray must be less than BaseException

# 2 all elemenmts of subarray are odd.
# and sum of all elemnts of the subaarray must be greter than B
# , Your taskj is to find the good subarrays in A



# n = len(A)
# for i in range(n):
#     for j in range (1, n):
#         subarray = A[j- i +1]
#         if all(n % 2 == 0 for x in subarray) or all (x % 2 )

arr = [1,2,3,4,5,6,7]
b = 10
count = 0
sum1 = 0
length = 0
for x in arr:
    sum1 += x
    length += 1
    if sum1 < b and length % 2 == 0:
        count += 1
    if sum1 > 0 and length % 2 != 0:
        count += 1
print(count)

# Ques = given a string is you have to count no. of AG pairs in a string , a string Contain of Capital letter only. 
# Str = "ABCGAG" 

# Str = "ABCGAG"
# count = 0

# for i in Str :





