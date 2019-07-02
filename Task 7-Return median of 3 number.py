#Adithya Krishnan
#Task 7-FInd median of 3 values
a=int(input("Value 1: "))
b=int(input("Value 2: "))
c=int(input("Value 3: "))
if c<=b<=a or a<=b<=c:
    median=b
elif b<=a<=c or c<=a<=b:
    median=a
else:
    median=c
print("Median is: ")
print(median)

