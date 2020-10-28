# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.__fabric = self.consumption()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 40:
            self.__size = 40
        elif value > 58:
            self.__size = 58
        else:
            self.__size = value

    def consumption(self):
        return round(self.__size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Для размера {self.__size} нужно {self.__fabric} ткани на пальто'


class Suit(Clothes):
    def __init__(self, length):
        self.length = length
        self.__fabric = self.consumption()

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 100:
            self.__length = 100
        elif value > 240:
            self.__length = 240
        else:
            self.__length = value

    def consumption(self):
        return round(self.__length * 2 + 0.3, 2)

    def __str__(self):
        return f'Для роста {self.__length} нужно {self.__fabric} ткани на костюм'


if __name__ == '__main__':
    coat_1 = Coat(12)
    suit_1 = Suit(23)
    print(coat_1)
    print(suit_1)
    coat_2 = Coat(123)
    suit_2 = Suit(253)
    print(coat_2)
    print(suit_2)
    coat_3 = Coat(45)
    suit_3 = Suit(157)
    print(coat_3)
    print(suit_3)
