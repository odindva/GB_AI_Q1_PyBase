# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""это итератор Б"""


from sys import argv
from itertools import cycle


def help_me():
    print('скрипт принимает от 0 до n параметров\n'
          'циклично генерируюет элементы некоторой строки\n'
          'первый параметр - длина списка (по умолчанию равен 10) - целое число\n'
          'второй и последующие параметры - строка (по умолчанию "abcdefghijklmnopqrstuvwxyz")\n'
          'параметры (2 - n) склеиваются символом "|"\n'
          'python hw_04_06(b).py 10 ABC DEF ---> [A, B, C, |, D, E, F, |, A, B]')


def gen_repeat(template="abcdefghijklmnopqrstuvwxyz", count_number=10):
    """итератор, повторяющий элементы некоторого списка, определенного заранее

    :param template: итерируемый объект для повторения элементов (по умолчанию "abcdefghijklmnopqrstuvwxyz")
    :param count_number: максимальное значение генераций (по умолчанию 10)
    :return: итератор
    """
    c = 0
    for el in cycle(template):
        if c >= count_number:
            break
        c += 1
        yield el


try:
    if len(argv) == 1:
        print(list(gen_repeat()))
    elif len(argv) == 2:
        print(list(gen_repeat(count_number=int(argv[1]))))
    else:
        print(list(gen_repeat(count_number=int(argv[1]), template=('|'.join(argv[2:])) + '|')))
except ValueError:
    help_me()
