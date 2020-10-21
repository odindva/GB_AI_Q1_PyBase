# 2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, length, width):
        """создать дорожное полотно

        :param length: длина полотна в метрах
        :param width: ширина полотна в метрах
        """
        self._length = length
        self._width = width

    def mass(self, thickness=1, mass_one=25, in_kg=False):
        """метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна

        :param in_kg: True, если результат нужен в кг,
        по умолчанию False: в тоннах
        :param thickness: толщина покрытия в см,
        по умолчанию 1
        :param mass_one: масса асфальта в кг для покрытия одного кв метра дороги асфальтом, толщиной в 1 см,
        по умолчанию 25
        :return: масса асфальта в тоннах
        """
        try:
            out = int(self._length * self._width * mass_one * thickness / (1 if in_kg else 1000))
            return out
        except TypeError as e:
            print(e)
            return None


road = Road(5000, 20)
print(road.mass())
print(road.mass(thickness=5))
print(road.mass(thickness=5, mass_one=30))
print(road.mass(thickness=5, mass_one=30, in_kg=True))
