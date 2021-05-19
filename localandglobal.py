x=20
def printx():
    global x                #Declaring global variable
    x=7
    print(x)
printx()
print(x)