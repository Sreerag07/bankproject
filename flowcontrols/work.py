sex=input("Enter male or female")
mstatus=input("Married or not")
if(sex=='M'):
    age = int(input("Enter the age"))
    if(20<=age<=40):
        print("Can work anywhere")
    elif(40<=age<=60):
        print("Only in urban areas")
    else:
        print("ERROR")
elif(sex=='F'):
    print("Only in urban areas")
else:
    print("Invalid input")