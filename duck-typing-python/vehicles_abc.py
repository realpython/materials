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
        print("The car is starting")

    def stop(self):
        print("The car is stopping")

    def drive(self):
        print("The car is driving")


class Truck(Vehicle):
    def start(self):
        print("The truck is starting")

    def stop(self):
        print("The truck is stopping")

    def drive(self):
        print("The truck is driving")
