"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    total_consumption = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.coat_consumption = self.consumption
        Clothes.total_consumption += self.consumption

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5, 3)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        self.suit_consumption = self.consumption()
        Clothes.total_consumption += self.consumption()

    def consumption(self):
        return round(2 * self.height + 0.3, 3)


clothes = Clothes
coat = Coat(10)
suit = Suit(10)


print(f'Coat material consumption is: {coat.coat_consumption}')
print(f'Suit material consumption is: {suit.suit_consumption}\n')
print(f'Total material consumption is: {Clothes.total_consumption}')

# out:
#   Coat material consumption is: 2.038
#   Suit material consumption is: 20.3
#
#   Total material consumption is: 22.338
