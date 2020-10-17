# 7) Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json


file_name = 'file_7.txt'
file_name_out = 'file_7.json'
dict_1 = dict()
average_profit = []
try:
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            words = line.split()
            try:
                dict_1[words[0]] = int(words[2]) - int(words[3])
                if dict_1[words[0]] >= 0:
                    average_profit.append(dict_1[words[0]])
            except ValueError:
                pass
            except IndexError:
                pass
except IOError:
    print('Ошибка ввод-вывода')

d = None
if average_profit:
    d = [dict_1, {"average_profit": sum(average_profit) / len(average_profit)}]

try:
    with open(file_name_out, 'w') as f:
        json.dump(d, f)
except IOError:
    print('Ошибка ввод-вывода')
