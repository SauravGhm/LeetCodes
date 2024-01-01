import datetime

class Car:
    def __init__(self, model, make):
        self.model = model
        self.make  = make

class Hoverboard:
    def __init__(self, flyskill, jumprate):
        self.flyskill  =  flyskill
        self.jumprate = jumprate

#creating objects by initializing with the class names

FastFly = Hoverboard("excellent", 100 )
FastCars = Car("lATEST", 600)

print(FastCars.model)
print(FastFly.jumprate)
