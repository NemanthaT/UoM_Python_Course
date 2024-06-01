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

while True:
    main()
    ch=input("Do you want to Add more cars? (y/n):")
    if ch=='y':
        main()
    elif ch=='n':
        break
    else:
        print("Invalid choice")
        print("Please enter valid choice")
        main()

print("Details of cars are as follows:")
for i in details:
    i.print_dete()
    print("----------------------")