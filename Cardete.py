class car:
    def __init__(self, name, year, model):
        self.name = name
        self.year = year
        self.model= model
    
    def print_dete(self):
        print("Car name=",self.name)
        print("Car manufactured year=",self.year)
        print("Car mode=",self.model)

details=[] #list to store car details

def main():
    name=input("Enter car name = ")
    year=input("Enter car year = ")
    model=input("Enter car model = ")

    car1=car(name,year,model)

    global details
    details.append(car1)
    global ch
    ch=input("Do you want to Add more cars? (y/n):")
    
print("Welcome to car details program")
print("\n")
print("Please enter the details of the car,")
print("\n")

while True:
    main()
    if ch=='y':
        main()
    elif ch=='n':
        break
    else:
        print("Invalid choice")
        print("Please enter valid choice")
        main()

print("----------------------")
print("Details of cars are as follows,")
print("\n")

for i in details:
    i.print_dete()
    print("----------------------")