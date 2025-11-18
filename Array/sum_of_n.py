 # # Q Write a program to solve to get sum of natural numbers.
# n=int(input("Enter a number :"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)    
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return sum(n-1)+n

# print(sum(3))

# Factorial 
def factorial(n):
    if n==1 or n==0:
        return 1
    return factorial(n-1)*n
    
print(factorial(5))    
