# recursion is a programming technique where a function calls itself directly or indirectly in order to solve a problem . In a recursive func the func makes ome ,kr,ore callls toh iyself as a part ofnitd fcutiojn . the process continue until a base case is reach at which point the func stop calling itself and `written a result.StopAsyncIteration
# write to program to calculate sum of natural numbers

Num = int(input("enter"))
for i in range (1,Num + 1):
    pr
    
    
#make a assumption , decide what your func does and trust that it will do it
# Solve the bigger prob using such prob , whhn your recursion stops

# calculate factorial with the help of recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

num = int(input("Enter a number: "))
print("Factorial =", fact(num))

#Write a program