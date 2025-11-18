#
# Arr = [16,]\
# Output = 17 , 5 and 2
#write a program to print all the leaders in the array an element in the leader if it is greater than all the elements to its right side and the right most element is always a leader for example 16, 17, 4, 3, 5, 2 output is 17, 5
arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
leaders = []
max_from_right = arr[-1]
leaders.append(max_from_right)

for i in range(n-2, -1, -1):
    if arr[i] > max_from_right:
        max_from_right = arr[i]
        leaders.append(max_from_right)

leaders.reverse()
print(*leaders)