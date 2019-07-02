#Adithya Krishnan
#Task 6 - Chk if triangle is eq,isosceles,scalene
a=int(input("Side 1: "))
b=int(input("Side 2: "))
c=int(input("Side 3: "))
if(c==b==a):
    print("Equilateral triangle")
elif(c==b or b==a or c==a):
    print("Isosceles triangle")
else:
    print("Scalene triangle")

