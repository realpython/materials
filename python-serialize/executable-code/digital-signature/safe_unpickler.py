import importlib
import io
import pickle


class SafeUnpickler(pickle.Unpickler):
    ALLOWED = {
        "builtins": ["print"],
        "sysconfig": ["get_python_version"],
    }

    @classmethod
    def safe_loads(cls, serialized_data):
        file = io.BytesIO(serialized_data)
        return cls(file).load()

    def find_class(self, module_name, name):
        if module_name in self.ALLOWED:
            if name in self.ALLOWED[module_name]:
                module = importlib.import_module(module_name)
                return getattr(module, name)
        raise pickle.UnpicklingError(f"{module_name}.{name} is unsafe")
