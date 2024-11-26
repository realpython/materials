from state_machine_base.base_state import BaseState

if __name__ == "__main__":
    current_state = BaseState()
    current_state = current_state.on_event("to_b")
