def print_employees(**kwargs):
    for k,v in kwargs.items():#taking as dictionary values(key value pairs)
        print(k,"=>",v)
print_employees(id=100,nat_place="pakkam")