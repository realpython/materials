from state_machine_controller.state_a import StateA
from state_machine_controller.state_b import StateB


class Controller:
    def __init__(self):
        self.state = StateA()

    def on_event(self, event):
        match event:
            case 'to_a':
                self.state = StateA()
            case 'to_b':
                self.state = StateB()
            case _:
                self.state = self.state
                