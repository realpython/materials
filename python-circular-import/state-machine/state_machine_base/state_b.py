from state_machine_base.base_state import BaseState


class StateB(BaseState):
    pass

BaseState.register_state('to_a', 'StateA')