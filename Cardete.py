class car: #class to store car details
    def __init__(self, name, year, model): #constructor to initialize car details
        self.name = name
        self.year = year
        self.model= model
    
    def print_dete(self): #function to print car details
        print("Car name=",self.name)
        print("Car manufactured year=",self.year)
        print("Car model=",self.model)

details=[] #list to store car details
con=True #to continue the program
def choice(): #function to get user choice
    global ch
    ch=input("Do you want to Add more cars? (y/n): ")
    if ch=='y': #if user wants to add more cars
        main()
    elif ch=='n': #if user does not want to add more cars
        global con
        con=False
        return con
    else: #if user enters invalid choice
        print("Invalid choice")
        print("Please enter valid choice")
        choice()

def delete(): #function to delete car details
    global details
    n=input("Enter car name to delete = ")
    m=input("Enter car model= ")
    for i in details:
        if i.name==n and i.model==m:
            details.remove(i)
            print("Car details deleted successfully")
            break
    else:
        print("Car not found")

def print_stack(): #function to print car details
    global details
    for i in details:
        i.print_dete()
        print("----------------------")

def main(): #function to get car details
    name=input("Enter car name = ")
    year=input("Enter car year = ")
    model=input("Enter car model = ")

    car1=car(name,year,model) #object of car class

    global details #to access global variable details
    details.append(car1)
    choice()
    
print("Welcome to car details program")
print("\n")
print("Please enter the details of the car,")
print("\n")

while con==True:
    main()

print("----------------------")
print("Details of cars are as follows,")
print("\n")

print_stack()

delete() #to delete car details
print("----------------------")
print("Details of cars are as follows,")
print_stack()