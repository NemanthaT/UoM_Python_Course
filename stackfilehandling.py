#Push function to push the elements in the stack
def push(stack,value):
    stack.append(value)

#Pop function to pop the elements from the stack
def pops(stack):
    stack.pop()

#Intializing the stack
myStack=[]

#Getting the number of elements to push
#inpt=int(input("Enter the number of elements you want to push: "))

#Opening the file in read mode
f=open("stackinput.txt","r")

inpt=0

#Pushing the elements in the stack
for i in f:
    value = int(i.strip())
    myStack.append(value)
    inpt+=1

#Closing the file
f.close()

#Printing the stack
print("Printing the stack, after pushing the elements.",myStack)

#Opening the file in write mode
f=open("stack.txt","w")
f.write(str(myStack))

#Searching the elements from the stack
srch=int(input("Enter the value that you want to search: "))

#Checking the element is present in the stack or not
if srch in myStack:
    print("Element is present in the stack.")
    print("What you want to do with the element?")
    print("     1.Nothing = No")
    print("     2.Change the element = Change")
    choice=input("Enter your choice: ")
    #Checking the choice

    if choice=="Change":
        index=myStack.index(srch)
        value=int(input("Enter the new value: "))
        myStack[index]=value
        print(myStack)
        f=open("stack.txt","w")
        f.write(str(myStack))

    elif choice=="No":
        print("Thank you")

    else:
        print("You have entered the wrong choice.")

else: 
    print("Element is not present in the stack.")

#Popping the elements from the stack
for i in range(inpt):
    pops(myStack)

#Printing the stack after popping the elements
print("After popping the elements:",myStack)

print("Terminating the program.")