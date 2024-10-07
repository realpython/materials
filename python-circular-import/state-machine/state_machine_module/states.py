class StateA:
    def on_event(self, event):
        if event == "to_b":
            return StateB()
        else:
            return self


class StateB:
    def on_event(self, event):
        if event == "to_a":
            return StateA()
        else:
            return self
