# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


file_name = 'file_4.txt'
file_name_out = 'file_4_out.txt'
lines = []
figures = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'zero': 'ноль'}
try:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except IOError:
    print('Ошибка ввод-вывода')

try:
    with open(file_name_out, 'w') as f:
        for line in lines:
            figure = figures[line.split()[0].lower()].title()
            f.write(figure + line[len(line.split()[0]):])
except IOError:
    print('Ошибка ввод-вывода')
