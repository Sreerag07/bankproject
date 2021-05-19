my_list=[11,3,2,4,7,88,1,-4,-10,-444,234,-432]
print(my_list)
new_list=[]
while my_list:
    min=my_list[0]
    for i in my_list:
        if i<min:
            min=i
    new_list.append(min)
    my_list.remove(min)
print(new_list)
my_list.sort()      #using sort keyword
print(my_list)