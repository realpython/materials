from abc import ABC, abstractmethod

class BaseInterface(ABC):
    """Abstract base class defining the interface."""

    @abstractmethod
    def do_something(self):
        pass

def create_instance(name):
    """Factory method to create instances of concrete implementations."""
    if name == 'A':
        from implementation_a import ImplementationA
        return ImplementationA()
    elif name == 'B':
        from implementation_b import ImplementationB
        return ImplementationB()
    else:
        raise ValueError(f"Unknown implementation '{name}'")