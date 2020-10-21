# 3) Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income=None):
        if income is None:
            income = {"wage": 11421, "bonus": 20000}
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income


class Position(Worker):
    def get_full_name(self):
        print(f'ФИО работника: {self.name} {self.surname}\nДолжность: {self.position}')

    def get_total_income(self):
        print(sum(self._Worker__income.values()))


p_1 = Position('a', 'b', 'c')
p_1.get_full_name()
p_1.get_total_income()

p_2 = Position('a', 'b', 'c', {"wage": 50000, "bonus": 50000})
p_2.get_full_name()
p_2.get_total_income()
