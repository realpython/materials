from state_machine_controller.controller import Controller

if __name__ == "__main__":
    controller = Controller()
    print(controller.state)
    controller.on_event("to_b")
    print(controller.state)
    controller.on_event("to_a")
    print(controller.state)
