dict={'name':'zara','age':7,'class':'first','place':'kasaragod'}
# flag=0
# for i in dict:
#     if i==ent:
#         flag=1
#         break
# if flag==1:
#     print("found")
# else:
#     print("not found")
def is_key_present(x):
    if x in dict:
        print("found")
    else:
        print("not found")
ent=input("Enter key")
is_key_present(ent)