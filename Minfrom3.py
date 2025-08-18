#Input three numbers and print the min number

A = int(input("enter No. For A"))
B = int(input("enter no. For B"))
C = int(input("Enter No. For C"))

if A < B and A < C :
    print("A is the minimum no.")

elif A == B or B== C :
    print("Two Numbers are equal")

elif B <  A and B < C :
    print("B is Minimum no. ")

else :
    print("C is minimum")        


#Q3  Given 5 number and print their average
A = int(input("enter No. For A"))
B = int(input("enter no. For B"))
C = int(input("Enter No. For C"))
D = int(input("Enter no. for D"))
E = int(input("enter no. for E "))

Sum_num =  Sum(A+B+C+D+E)

Avg = Sum_num / len(Sum_num)