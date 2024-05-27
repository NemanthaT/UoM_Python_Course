#TODO: Write the functions for arithmatic operations here

def add(a,b):
    return a+b
    
def substract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
    
def divide(a,b):
    if b==0:
         return "Zero Division Error"
    return a/b
    
def power(a,b):
    return a**b
    
def remainder(a,b):
    return a%b

#These functions should cover Task 2


#-------------------------------------
#TODO: Write the select_op(choice) function here
def select_op(choice,a,b):
    if choice=='+':
        return add(a,b)
    elif choice=='-':
        return substract(a,b)
    elif choice=='*':
        return multiply(a,b)
    elif choice=='/':
        return divide(a,b)
    elif choice=='^':
        return power(a,b)
    elif choice=='%':
        return remainder(a,b)
    ##elif choice=='$':
#This function sould cover Task 1 (Section 2) and Task 3




#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)



#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  a=1
  b=2
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  if(choice== '#'):
    #program ends here
    print("Done. Terminating")
    exit()
  ainput=input("Enter first number: ")    
  a=int(ainput)
  binput=input("Enter second number: ")
  b=int(binput)
  result=select_op(choice,a,b)
  if result=="Zero Division Error":
    print(float(a),choice,float(b),"=","None")
  else: print(float(a),choice,float(b),"=",float(result))