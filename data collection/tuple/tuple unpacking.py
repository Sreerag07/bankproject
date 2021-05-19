# my_tuple=1,1.3,"hello"
# a,b,c=my_tuple
# print(a)
# print(b)
# print(c)
tup=1,2,3
a,b,c=tup
print(a+b+c)
#we can also access the elements using the index values
print(tup[0])#1
#count keyword is used to find the number of one element
print(tup.count(1))
#index is used to find the index value of the element
print(tup.index(3))
#if elements are repeating the index of element in first position will be printed