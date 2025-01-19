class car:
    def __init__(self,brand,name,model,price):
        self.brand=brand
        self.name=name
        self.model=model
        self.price=price
    
    def display(self):
        print(f" Car Brand : {self.brand}")
        print(f' Car Name : {self.name}')
        print(f'Car Model : {self.model}')
        print(f'Car Price : {self.price}')

class detail:
    def __init__(self):
        self.detail=[]

    
    def add_car(self):
        brand=input("Enter your car Brand")
        name=input("Enter your Car Name")
        model=input("Enter your Car Model")
        price=input("Enter your Car Price")
        new_car=car(brand,name,model,price)
        self.detail.append(new_car)
        print("new car details added succesfully")

    def display_all(self):
        if not  self.detail:
            print("No car found")
        else:
            for car in self.detail:
                car.display()
    def menu(self):
        while 1:
            print("welcome to my car showroom")
            print("1 : Add New Car")
            print("2 : display all car")
            print("3 : exit")
            choice=input("enter your choice")
            if choice=="1":
                self.add_car()
            elif choice=="2":
                self.display_all()
            elif choice=="3":
                print("Exit Succesfully , Ram Ram ji")
            else:
                print("invalid input: please first add a car")



if __name__ == "__main__":
    detail = detail()
    detail.menu()
