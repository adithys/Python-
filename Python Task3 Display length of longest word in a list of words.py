#Adithya Krishnan
#Python Task-3 Accept a list of words and display the length of longest element

A=[]
n=int(input("No of elements in list: "))
for j in range(0,n):
    elem=input("Elem: "+ str(j+1) + ":")
    A.append(elem)
max=len(A[0])
temp=A[0]
for i in A:
    if(len(i)>max):
        max=len(i)
        temp=i
print("Word with longest length: ")
print(temp)
       
