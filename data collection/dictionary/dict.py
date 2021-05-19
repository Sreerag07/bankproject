dict={'name':'zara','age':7,'class':'first'}
print(dict)
#key value pairs
#key cannot be null
print(type(dict))
#using key we can access the value
print("name:",dict['name'])
print("age:",dict['age'])
#declaring empty dictionary
dic={}
print(dic)
print(type(dic))
#updating the values in dictionary
dict['age']=8
print(dict)
#adding new element
dict['school']="upschool"
print(dict)
#we can add dictionary using update keyword
dict.update({'location':'kochi'})
