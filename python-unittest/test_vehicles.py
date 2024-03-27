import unittest

import vehicles


class TestVehicles(unittest.TestCase):
    def test_vehicle_is_instance_of_car(self):
        car = vehicles.Car("Chevrolet", "Corvette", 194)
        self.assertIsInstance(car, vehicles.Car)

    def test_vehicle_is_instance_of_truck(self):
        truck = vehicles.Truck("Ford", "F-150", 2000)
        self.assertIsInstance(truck, vehicles.Truck)

    def test_vehicles_factory(self):
        car = vehicles.vehicle_factory(
            vehicles.Car,
            make="Toyota",
            model="Corolla",
            max_speed=180,
        )
        self.assertIsInstance(car, vehicles.Vehicle)


if __name__ == "__main__":
    unittest.main(verbosity=2)
