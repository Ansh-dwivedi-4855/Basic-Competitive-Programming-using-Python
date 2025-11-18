arr=[16,17,4,3,5,2]
result=[]
last=arr[-1]
result.append(last)
for i in range(len(arr)-2,0,-1):
    if arr[i]>last:
        result.append(arr[i])
        last=arr[i]
result.reverse()
print(result)        



    
    
    

