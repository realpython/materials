class BaseState:
    state_registry = {}

    @classmethod
    def register_state(cls, name, state_cls):
        cls.state_registry[name] = state_cls

    def on_event(self, event):
        next_state_cls = self.state_registry.get(event)
        if next_state_cls:
            return next_state_cls()
        return self
