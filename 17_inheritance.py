"""Inheritance in Python"""

class Vehicle: #Base class for all vehicles   
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

class Car(Vehicle): #Derived class for cars    
    def __init__(self, make, model, year, num_doors=4):
        super().__init__(make, model,year)
        self.num_doors = num_doors
    def resale_value(self):
        print("resale value is : xyz")
   
class Bike(Vehicle): #Derived class for Bikes
    def __init__(self, make, model,year, num_gears):
        super().__init__(make, model,year)
        self.num_gears = num_gears
    def resale_value(self):
        print("resale value is : xyz")
    def wheelie(self):
        return (f"{self.make} {self.model} is doing a wheelie!")
    
car1 = Car("Mustang GT", "Selby 650", 2020)
print(car1.make)  # Output: Mustang GT
print(car1.model)   # Output: Selby 650
print(car1.year)  # Output: 2020
print(car1.num_doors)  # Output: 4
car1.resale_value()  # Output: resale value is : xyz
car1.start()  # Output: Mustang GT Selby 650 is starting.
car1.stop()   # Output: Mustang GT Selby 650 is stopping.

bike1 = Bike("Royal Enfild", "GT Continental 650", 2021, 6)
print(bike1.make)  # Output: Royal Enfild
print(bike1.model)   # Output: GT Continental 650
print(bike1.year)  # Output: 2021
print(bike1.num_gears)  # Output: 6
bike1.resale_value()  # Output: resale value is : xyz
bike1.start()  # Output: Royal Enfild GT Continental 650 is starting.
bike1.stop()   # Output: Royal Enfild GT Continental 650 is stopping.
print(bike1.wheelie())  # Output: Royal Enfild GT Continental 650 is doing a wheelie!
      #in class Bike useing return so i have to use print.