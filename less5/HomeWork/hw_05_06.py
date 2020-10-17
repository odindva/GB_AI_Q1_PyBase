# 6) Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                      Физика:   30(л)   —   10(лаб)
#                      Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
from functools import reduce
from typing import re


def only_digits(string):
    """Возвращает целое число из строки, игнорируя всё лишнее

    :param string:
    :return: целое число из строки или 0, если цифр в строке нет
    """
    result = ''.join([ch for ch in string if ch.isdigit()])
    return int(result) if result else 0


file_name = 'file_6.txt'
lines = []
dict_1 = dict()
try:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except IOError:
    print('Ошибка ввод-вывода')

for line in lines:
    dict_1[line.split()[0].replace(':', '')] = sum([only_digits(s) for s in line.split()[1:]])

print(dict_1)
