# import re
#
# n=input("Enter the number")
# x='[A-Z]{2}[\d]{2}[A-Z]{1}[\d]{4}$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
import re

n=input("Enter the number")
x='[A-Za-z0-9][@][g][m][a][i][l][.][c][o][m]$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")