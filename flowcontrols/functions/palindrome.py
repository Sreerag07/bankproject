a=input("Enter a word")
temp=a
for i in a:
    rev=a[::-1]
if(rev==temp):
    print("Is palindrome")
else:
    print("Not a palindrome")