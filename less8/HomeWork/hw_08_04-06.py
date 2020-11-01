# 4) Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5) Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
from random import randint
from copy import copy, deepcopy


class OfficeEquipment:
    def __init__(self, name, prise, weight, count):
        self.name = name
        self.prise = prise
        self.weight = weight
        self.count = count

    def __str__(self):
        return f'{type(self)}||name: {str(self.name)}, prise: {str(self.prise)}, ' \
               f'weight: {str(self.weight)}, count: {str(self.count)}||'

    def __repr__(self):
        return f'{type(self)}||name: {str(self.name)}, prise: {str(self.prise)}, ' \
               f'weight: {str(self.weight)}, count: {str(self.count)}||'


class Printer(OfficeEquipment):
    def print_(self, param=''):
        print(f'{self.name} printed: {param}')


class Scanner(OfficeEquipment):
    def scan(self):
        print(f'{self.name} scanned: {[randint(1,1000) for _ in range(10)]}')


class Xerox(OfficeEquipment):
    def copy(self, obj='something'):
        print(f'{self.name} copied: {obj}')


class Company:
    def __init__(self, name, storage, departments=None):
        if departments is None:
            departments = dict()  # пичарм, почему-то, подсказал сделать так, а не в скобках
        self.__name = name
        self.storage = storage
        self.__departments = departments

    def get_name(self):
        return copy(self.__name)

    def get_departments(self):
        return deepcopy(self.__departments)

    def department(self, name_d):
        return self.__departments[name_d]

    def add_department(self, department):
        self.__departments[department] = {}


class Storage:

    def __init__(self):
        # Пока, конкретные ключи:
        self.__equipments = {'Printers': dict(dict()), 'Scanners': dict(dict()), 'Xeroxes': dict(dict())}

    def __str__(self):
        return str(self.__equipments)

    @staticmethod
    def input_params():
        try:
            name = input('input name: ')
            prise = float(input('input prise: '))
            weight = float(input('input weight: '))
            count = int(input('input count: '))
            if prise < 0 or weight < 0 or count < 0:
                raise ValueError
        except (ValueError, TypeError):
            print("Incorrect value!")
        else:
            return name, prise, weight, count
        return None

    def add(self):
        while True:
            command = input('\n1 - printer, 2 - scanner, 3 - xerox, 0 - exit\n input number to add: ')
            if not command or command == '0':
                break
            else:
                if command in ['1', '2', '3']:
                    params = Storage.input_params()
                else:
                    continue
                group = None
                if command == '1':
                    group = 'Printers'
                elif command == '2':
                    group = 'Scanners'
                elif command == '3':
                    group = 'Xeroxes'
                if params:
                    if params[0] in self.__equipments[group]:
                        self.__equipments[group][params[0]].prise = params[1]
                        self.__equipments[group][params[0]].weight = params[2]
                        self.__equipments[group][params[0]].count += params[3]
                    else:
                        self.__equipments[group][params[0]] = Printer(*params)

    def move(self, department, count: int, group='Printers'):
        """
        Перемещает со склада первые попавшиеся объекты из указанной группы в отдел 'department' в количестве 'count'
        """
        equipments = deepcopy(self.__equipments[group])
        results = []
        for k, v in equipments. items():
            if count < int(str(v.count)):
                self.__equipments[group][k].count -= count
                v.count = count
                results.append(v)
                break
            elif count == int(str(v.count)):
                results.append(self.__equipments[group].pop([k]))
                break
            else:
                results.append(self.__equipments[group].pop([k]))
                count -= v.count
        for result in results:
            department[group] = dict()
            department[group][result.name] = result


if __name__ == '__main__':
    storage_1 = Storage()
    company = Company('Company_1', storage_1, {'Accounts': {}, 'Project': {}})
    company.add_department('Management')
    print('1) departments', company.get_departments())
    storage_1.add()
    print('2) storage_1', storage_1)
    storage_1.move(company.department('Management'), 1)
    print('3) departments', company.get_departments())
    for printer in company.department('Management')['Printers'].values():
        printer.print_('test print in this department')
