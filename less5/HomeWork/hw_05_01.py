# 1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


file_name = 'file_1.txt'
try:
    with open(file_name, 'w', encoding='utf-8') as f:
        while True:
            s = input(f'Введите строку для добавления в файл {file_name} или Enter для выхода: ')
            if not s:
                break
            else:
                f.write(s + '\n')
except IOError:
    print('Ошибка ввод-вывода')
