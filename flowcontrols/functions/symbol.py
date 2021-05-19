char=input("Enter a string")
b=""
for i in char:
    if i not in("!@#$%^&*()_+{}|:;?/"):
        b+=i
print(b)
