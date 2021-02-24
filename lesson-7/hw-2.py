from abc import ABC, abstractmethod

class MyAbsctractClass(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes, MyAbsctractClass):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size/6.5 + 0.5


class Suit(Clothes, MyAbsctractClass):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_consumption(self):
        return self.height * 2 + 0.3


clothes1 = Coat("coat1", 6.5)
print(clothes1.fabric_consumption)

clothes2 = Suit("suit1", 2)
print(clothes2.fabric_consumption)
