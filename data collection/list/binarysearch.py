my_list=[5,2,1,4,9,88,77,33,7]
print(my_list)
my_list.sort()
# while my_list:
#     min=my_list[0]
#     for i in my_list:
#         if i<min:
#             min=i
#     new_list.append(min)
#     my_list.remove(min)
print(my_list)
num = int(input("enter input"))
low=0
high=len(my_list)-1
flag=0
while low<=high:
    mid=(low+high)//2
    if num>my_list[mid]:
        low=mid+1
    elif num<my_list[mid]:
        high=mid-1
    elif num==my_list[mid]:
        flag=1
        break
if flag==1:
    print("Element found")
else:
    print("Not found")

