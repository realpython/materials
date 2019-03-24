class Vehicle:

 def __init__(self, color, model):
    self.color = color
    self.model = model

class Device:

    def __init__(self):
        self.voltage = 12

class Car(Vehicle, Device):

    wheels = 0

    def __init__(self, color, model, year):
    Vehicle.__init__(self, color, model)
    Device.__init__(self)
    self.year = year

    def add_wheels(self, wheels):
        self.wheels = wheels

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, volts):
        print("Warning: this can cause problems!")
        self._voltage = volts

    @voltage.deleter
    def voltage(self):
        print("Warning: the radio will stop working!")
        del self._voltage

    def __str__(self):
        return f'Car {self.color} : {self.model} : {self.year}'

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __add__(self, other):
        return Car(self.color + other.color,
               self.model + other.model, int(self.year) + int(other.year))
