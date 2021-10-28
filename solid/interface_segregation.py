# ISP

from abc import ABC, abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    """
    For this kind of class, extend the Machine class will work well because
    the current class will use all the methods of its parent class.

    No method will not be overwritten.
    """

    def print(self, document):
        print("Printing!")

    def scan(self, document):
        print("Scanning!")

    def fax(self, document):
        print("Faxing!")


class SimplePrinter(Machine):
    """
    When extends the Machine class i need to implement
    the methods print, scan and fax otherwise will throw an exception.

    This is bad because the Printer only need the print method, and
    the other methods will be available for calling, even with no use.
    """

    def print(self, document):
        print("Printing!")

    def scan(self, document):
        pass

    def fax(self, document):
        pass


# To solve this type of problem is recommended to create interfaces for each method!
# An example bellow!

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


# Now we just need to extend the parent classes we want!

class PrinterAndScanner(Scanner, Printer):
    def print(self, document):
        print("Printing!")

    def scan(self, document):
        print("Scanning!")


if __name__ == "__main__":
    printer_and_scanner = PrinterAndScanner()
    printer_and_scanner.print(None)
    printer_and_scanner.scan(None)
