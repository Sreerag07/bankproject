lst=[]
size = int(input("enter size"))
n=0
top=0
def push():
    global top,size
    if (top>=size):
        print("Stack is full")
    else:
        p=int(input("Enter the element to push"))
        lst.append(p)
        top+=1
def pop():
    global top,size
    if (top<= 0):
        print("stack is empty")
    else:
        a=input("Enter element to remove")
        lst.pop()
        top-=1
def display():
    print(lst)
while(n!=1):
    print("Enter the operation want to perform")
    opt=int(input("Enter 1)push2)pop3)display"))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    elif(opt==3):
        display()
    n=int(input("Press 1 for exit"))