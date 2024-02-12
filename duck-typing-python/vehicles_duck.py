class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

    def drive(self):
        print("Car is driving")


class Truck:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("Truck is starting")

    def stop(self):
        print("Truck is stopping")

    def drive(self):
        print("Truck is driving")
