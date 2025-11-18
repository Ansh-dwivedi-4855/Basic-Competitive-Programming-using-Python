
N = int(input("Enter a number : "))
nums = list(map(int, input().split()))
max_ending = nums[0]
max_so_far = nums[0]

for i in range(1, N):
    max_ending = max(nums[i], max_ending + nums[i])
    max_so_far = max(max_so_far, max_ending)

print(max_so_far)
