#Adithya Krishnan
#Python task-2 print file extension of the file entered by the user
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
