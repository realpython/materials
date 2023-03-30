class Aircraft:
    def __init__(self, thrust, lift, max_speed):
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed

    def technical_specs(self):
        print(f"Thrust: {self.thrust} kW")
        print(f"Lift: {self.lift} kg")
        print(f"Max speed: {self.max_speed} km/h")


class Helicopter(Aircraft):
    def __init__(self, thrust, lift, max_speed, num_rotors):
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors

    def technical_specs(self):
        super().technical_specs()
        print(f"Number of rotors: {self.num_rotors}")
