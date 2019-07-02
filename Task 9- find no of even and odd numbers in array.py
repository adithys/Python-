#Adithya Krishnan
#Python-Task 9-Count no of even and odd numbers
A=[]
n=int(input("Array size: "))
for i in range(0,n):
    elem=int(input("Element " + str(i+1) + ":"))
    A.append(elem)
evenct=0
oddct=0
for j in A:
    if j%2==0:
        evenct=evenct+1
    else:
        oddct=oddct+1
print("Even numbers in array: ")
print(evenct)
print("Odd numbers in array: ")
print(oddct)
