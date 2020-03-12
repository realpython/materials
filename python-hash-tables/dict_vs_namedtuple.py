from collections import namedtuple
Car = namedtuple('Car', ['name', 'color', 'size'])
car_tuple = Car(name="Toyota", color="black", size="big")
car_dict = {"name": "Toyota", "color": "black", "size": "big"}
