from abc import ABC, abstractmethod

# Bad example
# class Printer(ABC):
#     """Printer interface."""

#     @abstractmethod
#     def print(self, document):
#         pass

#     @abstractmethod
#     def fax(self, document):
#         pass

#     @abstractmethod
#     def scan(self, document):
#         pass


# class OldPrinter(Printer):
#     """Old printer, concrete implementation."""

#     def print(self, document):
#         print(f"Print {document} in black and white")

#     def fax(self, document):
#         raise NotImplementedError("Fax functionality not supported")

#     def scan(self, document):
#         raise NotImplementedError("Scan functionality not supported")


# class ModernPrinter(Printer):
#     """Modern printer, concrete implementation."""

#     def print(self, document):
#         print(f"Printing {document} in color")

#     def fax(self, document):
#         print(f"Faxing {document}")

#     def scan(self, document):
#         print(f"Scanning {document}")


# Good example
class Printer(ABC):
    """Printer interface."""

    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    """Fax interface."""

    @abstractmethod
    def fax(self, document):
        pass


class Scan(ABC):
    """Scan interface."""

    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    """Old printer, concrete implementation."""

    def print(self, document):
        print(f"Print {document} in black and white")


class NewPrinter(Printer, Fax, Scan):
    """New printer, concrete implementation."""

    def print(self, document):
        print(f"Printing {document} in color")

    def fax(self, document):
        print(f"Faxing {document}")

    def scan(self, document):
        print(f"Scanning {document}")
        print(f"Scanning {document}")
