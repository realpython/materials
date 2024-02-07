from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    @abstractmethod
    def start(self):
        raise NotImplementedError("This method must be implemented")

    @abstractmethod
    def stop(self):
        raise NotImplementedError("This method must be implemented")

    @abstractmethod
    def drive(self):
        raise NotImplementedError("This method must be implemented")


class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

    def drive(self):
        print("Car is driving")


class Truck(Vehicle):
    def start(self):
        print("Truck is starting")

    def stop(self):
        print("Truck is stopping")

    def drive(self):
        print("Truck is driving")
