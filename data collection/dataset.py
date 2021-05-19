#set will not follow the order we given
# s={1,9,7,4}
# print(s)
#type is printed using type of keyword
# a="abc"
# print(type(a))
#defining an empty set using set()
# s=set()
# s.add(9)
# s.add("Hello")
# s.add(0.1)
# s.add(True)
# print(s)
# print(type(s))
#Set can contain different type of data in same set
# s=set()
# n=int(input("Enter number of element"))
# for i in range(0,n):
#     num=int(input("Enter number"))
#     s.add(num)
# print(s)
#Duplication of elements will not be supported
# remove() keyword is used to remove one element from set
#clear() keyword is used to delete all the elements from the set
s={1,2,3,5,6}
print(s)
s.remove(3)
print(s)
s.clear()
print(s)
# del s
# print(s)
s={{1,2,3},{2,3,4}}
print(s)
#does  not support nested set operations
