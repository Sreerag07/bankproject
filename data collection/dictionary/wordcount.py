a={}
x=input("Enter the words")
words=x.split(" ")#used to split words using the spaces between them
count=0
for word in words:
    if word not in a:
        a.update({word:1})
    else:
        val=int(a[word])
        val+=1
        a.update({word:val})
print(a)

