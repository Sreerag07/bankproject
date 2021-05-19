#list comprehension are used for creating new lists from other iterables
#as list comprehension return lists,they consists of brackets containing the expressions
#which is created for each element along with the for loop to iterate over each element
# lst=[1,2,3,4,5,6]
# print(lst)
# m=[]
# for i in lst:
#     m.append(i**2)
# print(m)
# lst=[1,2,3,4,5,6]
# m=[i*i for i in lst]
# print(m)
# fruits=["mango","apple","orange"]
# pairs=[ (fruit,fruit) for fruit in fruits]
# print(pairs)
# lst1=[1,2]
# lst2=[10,20]
# lst3=[(i,j) for i in lst1 for j in lst2 ]
# print(lst3)

lst=[10,11,12,13,14]
lst1=[i for i in lst if i%2==0]
print(lst1)

lst2=[7,8,9,4,2]
a=[num+1 if num>5 else num-1 for num in lst2]
print(a)



