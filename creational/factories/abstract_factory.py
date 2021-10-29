# Abstract Factory example

from abc import ABC, abstractmethod


class Mobile(ABC):

    @abstractmethod
    def get_signal(self):
        pass


class SamsungA9(Mobile):

    def get_signal(self):
        print("This is the signal of SamsungA9")


class SamsungS20(Mobile):

    def get_signal(self):
        print("This is the signal of SamsungS20")


class RedmiNote10(Mobile):

    def get_signal(self):
        print("This is the signal of RedmiNote10")


class Mi10(Mobile):

    def get_signal(self):
        print("This is the signal of Mi10")


class MobileFactory(ABC):

    @abstractmethod
    def get_mobile_first(self) -> Mobile:
        pass

    @abstractmethod
    def get_mobile_second(self) -> Mobile:
        pass


class SamsungFactory(MobileFactory):

    def get_mobile_first(self):
        return SamsungS20()

    def get_mobile_second(self):
        return SamsungA9()


class XiaomiFactory(MobileFactory):

    def get_mobile_first(self):
        return RedmiNote10()

    def get_mobile_second(self):
        return Mi10()


if __name__ == "__main__":
    factory: MobileFactory = SamsungFactory()
    factory2: MobileFactory = XiaomiFactory()

    factory.get_mobile_first().get_signal()
    factory.get_mobile_second().get_signal()

    factory2.get_mobile_first().get_signal()
    factory2.get_mobile_second().get_signal()