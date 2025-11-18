arr=[3,-1,4]
ans=0
for i in range(len(arr)):
    sum=0
    for j in range(len(arr)):
        sum=sum+arr[j]
        ans=ans+sum
print(ans)        

