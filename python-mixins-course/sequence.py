from abc import ABC, abstractmethod


class Sequence(ABC):
    @abstractmethod
    def __getitem__(self, index):
        pass

    @abstractmethod
    def __len__(self):
        pass