#map function can be use to apply some function to every object
#filter to select upon a condition
arr=[2,3,4,5,6]
#find squares
def square(num):
    return num**2
#map
squarelist=list(map(square,arr))
print(squarelist)
#using lambda
squarelist=list(map(lambda num:num**2,arr))
print(squarelist)
