# Function to perform arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("float division by zero")
        return "None"

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

# Initialize list to store history
history_list = []
# Function to handle operations and history
def select_op(choice):
    global history_list
    
    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif choice == '?':
        # Display history
        if not history_list:
            print("No past calculations to show")
        else:
            for item in history_list:
                print(item)
    elif choice in ('+', '-', '*', '/', '^', '%'):
        # Prompt for numbers
        while True:
            num1s = input()
            print("Enter first number:",num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1
            try:
                num1 = float(num1s)
                break
            except ValueError:
                print("Not a valid number, please enter again")
        
        while True:
            num2s = input()
            print("Enter second number:",num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                global num2
                num2 = float(num2s)
                break
            except ValueError:
                print("Not a valid number, please enter again")

        # Perform operation
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Something Went Wrong")
            return

        # Store in history
        history_item = f"{num1} {choice} {num2} = {result}"
        history_list.append(history_item)
        
        # Print result
        print(history_item)
    else:
        print("Unrecognized operation")

# Main loop
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
    print("8.History  : ? ")
    
    # Take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    ##if (num2==0):
        ##print("float division by zero")
    if select_op(choice) == -1:
        # Program ends here
        print("Done. Terminating")
        break