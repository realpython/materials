import abc
import sys
import sysconfig

import _testinternalcapi


class Feature(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        if self.supported:
            if self.enabled:
                return f"{self.name}: enabled \N{SPARKLES}"
            else:
                return f"{self.name}: disabled"
        else:
            return f"{self.name}: unsupported"

    @property
    @abc.abstractmethod
    def supported(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def enabled(self) -> bool:
        pass


class FreeThreading(Feature):
    def __init__(self) -> None:
        super().__init__("Free Threading")

    @property
    def supported(self) -> bool:
        return sysconfig.get_config_var("Py_GIL_DISABLED") == 1

    @property
    def enabled(self) -> bool:
        return not self.gil_enabled()

    def gil_enabled(self) -> bool:
        if sys.version_info >= (3, 13):
            return sys._is_gil_enabled()
        else:
            return True


class JitCompiler(Feature):
    def __init__(self):
        super().__init__("JIT Compiler")

    @property
    def supported(self) -> bool:
        return "_Py_JIT" in sysconfig.get_config_var("PY_CORE_CFLAGS")

    @property
    def enabled(self) -> bool:
        if sys.version_info >= (3, 13):
            return _testinternalcapi.get_optimizer() is not None
        else:
            return False
