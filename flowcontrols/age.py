dobyear=int(input("Enter year"))
dobmonth=int(input("Enter month"))
dobdate=int(input("Enter date"))
cyear=int(input("Enter current year"))
cmonth=int(input("Enter current month"))
cdate=int(input("Enter current date"))
dyear=cyear-dobyear
dmonth=cmonth-dobmonth
ddate=cdate-dobdate
if(dyear>=1):
    if(dmonth>=0):
        if(ddate>=0):
            print("age:",dyear,"years",dmonth,"months",ddate,"days")
        else:
            dmonth-=1
            ddate=31+ddate
            print("age:", dyear, "years", dmonth, "months", ddate, "days")
    elif(dmonth<0):
        if(ddate>=0):
            dyear-=1
            dmonth=dmonth+12
            ddate=ddate
            print("age:", dyear, "years", dmonth, "months", ddate, "days")
        else:
            dyear=dyear-1
            dmonth=dmonth-1
            dmonth=dmonth+12
            ddate=ddate+31
            print("age:", dyear, "years", dmonth, "months", ddate, "days")
    else:
        print("Error")
elif(dyear==0):
    if(dmonth<=0):
        if(ddate<=0):
            print("Error")
        else:
            print("age:", dyear, "years", dmonth, "months", ddate, "days")
    elif(dmonth>0):
        if(ddate<=0):
            dmonth-=1
            ddate=ddate+31
            print("age:", dyear, "years", dmonth, "months", ddate, "days")
        else:
            print("age:", dyear, "years", dmonth, "months", ddate, "days")
    else:
        print("Error")
else:
    print("Invalid input")