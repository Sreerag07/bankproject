salary=int(input("Enter salary"))
year=int(input("Enter year of service"))
if(year>5):
    salary+=(5/100)*salary
    print("salary is",salary)
else:
    print("Salary is",salary)