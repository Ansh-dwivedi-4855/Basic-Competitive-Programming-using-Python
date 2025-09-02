#For reverse Pattern
Num = int(input("Enter the Number :"))
for i in range (1,Num+1):
    for j in range(Num+1 -i):
        print("*", end = " ")
    print()  
    
       