held=int(input("Enter number of classes held"))
present=int(input("Enter number of class attended"))
avg=(present/held)*100
print("Percentage is",avg)
if(avg<75):
    print("Cannot be permitted")
else:
    print("Can enter")