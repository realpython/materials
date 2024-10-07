from state_machine_base.base_state import BaseState


class StateA(BaseState):
    pass


BaseState.register_state("to_b", "StateB")
