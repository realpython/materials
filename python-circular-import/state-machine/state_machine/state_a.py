from state_machine.state_b import StateB


class StateA:
    def on_event(self, event):
        if event == 'to_b':
            return StateB()
        else:
            return self