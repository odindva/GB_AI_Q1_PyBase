# 6)  *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }


data = []
keys_data = ('название', 'цена', 'количество', 'единица измерения')
id_data = 0
stop_word = 'q'
exit_word = 'e'
add_word = '+'
adds_word = '++'
view_word = 'v'
analytics_word = 'a'
delete_word = '-'

while True:
    command = input(f'\nДля завершения работы программы введите "{exit_word}"'
                    f'\nДля добавления товара введите "{add_word}"'
                    f'\nДля просмотра базы товаров введите "{view_word}"'
                    f'\nДля просмотра аналитики товаров введите "{analytics_word}"'
                    f'\nДля удаления товара введите "{delete_word}id", где id - индекс товара'
                    f'\n\nКоманда: ')

    if command == exit_word:
        break

    elif command == add_word:
        id_data += 1
        name = input(f'{keys_data[0]}: ')
        price, count = 0, 0
        while True:
            try:
                price = int(input(f'{keys_data[1]}: '))
                break
            except ValueError:
                print('Вы ввели не число')
        while True:
            try:
                count = int(input(f'{keys_data[2]}: '))
                break
            except ValueError:
                print('Вы ввели не число')
        unit = input(f'{keys_data[3]}: ')
        data.append((id_data, {keys_data[0]: name, keys_data[1]: price, keys_data[2]: count, keys_data[3]: unit}))
        print('Товар добавлен')

    elif command == view_word:
        print(*data, sep='\n')
        print()

    elif command == analytics_word:
        analytics = {}
        for key in keys_data:
            analytics[key] = []
            for item in data:
                analytics[key].append(item[1].get(key))
            analytics[key] = list(set(analytics.get(key)))
        for k, v in analytics.items():
            print(f'{k}: {v}')

    elif command[0] == delete_word:
        try:
            command = int(command[1:])
            if command < 1:
                raise ValueError
        except ValueError:
            print('Некорректный ввод')
            break
        print(f'Удалён товар {data.pop(command)}')
