#flow controls are used to control flow of program
#decision making-(if,if......else,if....elif....else)
#looping-(for,while)
#jumping-(break,continue,pass)
#1decision making
#..................
# if(condition):
#     stmnt1
#     stmnt2
#     .....
#     stmntn
# else:
#     stmnt
# ...................
age=int(input("enter the age"))
if(age>=18):
    print("You can vote")
else:
    print("You can't vote")