#Adithya Krishnan
#Python Task#5 Convert the given month into no of days
print("List of months: January February March April May June July August September October November December")
monthname=input("Enter the month: ")
if(monthname=="February"):
    print("No of days: 28 days in non-leap year, 29 in leap-year")
elif monthname in("April","June","September","November"):
    print("No of days: 30 ")
elif monthname in("January","March","May","July","August","October","December"):
    print("No of days: 31 ")
else:
    print("Wrong month.")
