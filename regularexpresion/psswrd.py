# import re
#
# n=input("Enter the number")
# x="([a-zA-Z]+\d$)"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
# import re
#
# n=input("Enter the number")
# x="^a[a-zA-Z0-9\w]*b$"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
import re

n=input("Enter the number")
x="([\D]{8,15}$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")