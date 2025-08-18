A = int(input("enter the number for A:"))
B = int(input("Enter The Number for B:"))
C = int(input("enter The Number For C:"))

if A == B or A == C or B == C :
    print("Two Number are equal")

elif A > B and B > C :
    print("A is Maximum") 

elif B > A and B > C :
    print(" B is maximum")

else :
    print("C is maximum")


