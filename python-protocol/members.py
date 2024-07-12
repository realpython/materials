from abc import abstractmethod
from typing import ClassVar, Protocol


class ProtocolMembersDemo(Protocol):
    class_attribute: ClassVar[int]
    instance_attribute: str

    def instance_method(self, arg: int) -> str: ...

    @classmethod
    def class_method(cls) -> str: ...

    @staticmethod
    def static_method(arg: int) -> str: ...

    @property
    def property_name(self) -> str: ...

    @property_name.setter
    def property_name(self, value: str) -> None: ...

    @abstractmethod
    def abstract_method(self) -> str: ...
