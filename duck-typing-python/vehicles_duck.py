class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("The car is starting")

    def stop(self):
        print("The car is stopping")

    def drive(self):
        print("The car is driving")


class Truck:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("The truck is starting")

    def stop(self):
        print("The truck is stopping")

    def drive(self):
        print("The truck is driving")
