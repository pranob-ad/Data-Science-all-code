class Dog:
    def __init__ (self, name, breed):
        self.name = name
        self.breed = breed

    def any_fn(self):
        print(f"{self.name} says Woof!")

dog = Dog("buddy", "Labrador")
print(dog.name)  # Output: buddy
print(dog.breed)  # Output: Labrador
dog.any_fn()  # Output: buddy says Woof!

class Car:
    def __init__(self, make , model, year):
        self.make = make
        self.model = model
        self.year = year

    def resale_value(self):
            print("resale value is : xyz")

    def start_engine(self):
                print("Engine started")

    def stop_engine(self):
                print("Engine stopped")

car1 = Car("Toyota", "Innova", 2020)
print(car1.make)  # Output: Toyota
print(car1.model)  # Output: Innova
print(car1.year)  # Output: 2020
car1.resale_value()  # Output: resale value is : xyz
car1.start_engine()  # Output: Engine started
car1.stop_engine()  # Output: Engine stopped

car2 = Car("Mustang", "GT Selby650", 2021)
print(car2.make)  # Output: Honda
print(car2.model)  # Output: Selby650
print(car2.year)  # Output: 2021
car2.resale_value()  # Output: resale value is : xyz
car2.start_engine()  # Output: Engine started
car2.stop_engine()  # Output: Engine stopped