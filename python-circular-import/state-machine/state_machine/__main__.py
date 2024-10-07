from state_machine.state_a import StateA

if __name__ == "__main__":
    current_state = StateA()
    current_state = current_state.on_event('to_b')