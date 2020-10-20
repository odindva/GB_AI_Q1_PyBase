# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce
from random import randint


file_name = 'file_5.txt'
lines = [str(randint(1, 20)) + ' ' for _ in range(10)]
# print(lines)
try:
    with open(file_name, 'w+') as f:
        f.writelines(lines)
        f.seek(0)
        print(reduce(lambda x, y: int(x) + int(y), f.readline().split()))  # подчеркивает "f.readline().split()", но работает"
except IOError:
    print('Ошибка ввод-вывода')
