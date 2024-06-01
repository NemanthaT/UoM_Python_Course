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

def choice(): #function to get user choice
    global ch
    ch=input("Do you want to Add more cars? (y/n): ")

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

while True:
    main()
    if ch=='y': #if user wants to add more cars
        main()
    elif ch=='n': #if user does not want to add more cars
        break
    else: #if user enters invalid choice
        print("Invalid choice")
        print("Please enter valid choice")
        choice()

print("----------------------")
print("Details of cars are as follows,")
print("\n")

for i in details: #to print car details
    i.print_dete()
    print("----------------------")