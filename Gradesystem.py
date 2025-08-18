# Grading System

Marks = int(input("Enter Your Marks"))
if (Marks < 0 or Marks > 100):
    print("Invalid Marks")
elif (Marks >= 90):
  print("Grade A")
elif (Marks >= 80 and  Marks <= 89 ):
 print("Grade B")
elif ( Marks >= 70 and Marks <= 79 ):
 print("Grade C")
elif ( Marks >= 60 and Marks <= 69 ):
 print("Grade D")
elif (Marks < 60):
  print ("Fail")
