from state_machine.state_a import StateA


class StateB:
    def on_event(self, event):
        if event == "to_a":
            return StateA()
        else:
            return self
