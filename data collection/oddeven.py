s={1,2,3,4,5,6,8,9,44,55,22,11,88}
odd=set()
even=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print("odd numbers:",odd)
print("Even numbers:",even)