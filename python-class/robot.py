class IndustrialRobot:
    def __init__(self):
        self.body = Body()
        self.arm = Arm()

    def rotate_body_left(self):
        self.body.rotate_left()

    def rotate_body_right(self):
        self.body.rotate_right()

    def move_arm_up(self):
        self.arm.move_up()

    def move_arm_down(self):
        self.arm.move_down()

    def weld(self):
        self.arm.weld()


class Body:
    def __init__(self):
        self.rotation = 0

    def rotate_left(self, degrees=10):
        self.rotation -= degrees
        print(f"Rotating body {degrees} degrees to the left...")

    def rotate_right(self, degrees=10):
        self.rotation += degrees
        print(f"Rotating body {degrees} degrees to the right...")


class Arm:
    def __init__(self):
        self.position = 0

    def move_up(self, distance=1):
        self.position += 1
        print(f"Moving arm {distance} cm up...")

    def move_down(self, distance=1):
        self.position -= 1
        print(f"Moving arm {distance} cm down...")

    def weld(self):
        print("Welding...")
