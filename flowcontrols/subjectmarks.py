num1=int(input("Enter mark1"))
num2=int(input("Enter mark2"))
num3=int(input("Enter mark3"))
num4=int(input("Enter mark4"))
total=num1+num2+num3+num4
print("total is",total)
if(180<=total<=200):
    print("A+ grade")
elif(160<=total<=179):
    print("A grade")
elif(140<=total<=159):
    print("B+ grade")
elif(120<=total<=139):
    print("B grade")
elif(100<=total<=119):
    print("C+ grade")
elif(80<=total<=99):
    print("C grade")
else:
    print("D+grade")