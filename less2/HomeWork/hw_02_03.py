# 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


months = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

# while True:
#     try:
#         month = int(input('Введите номер месяца: '))
#         if month < 1 or month > 12:
#             raise ValueError
#         break
#     except ValueError:
#         print('Вы ввели не номер месяца')

while True:
    month = input('Введите номер месяца: ')
    if month.isdigit():
        month = int(month)
        if 1 <= int(month) <= 12:
            break
    print('Вы ввели не номер месяца (1 - 12)')

for key, val in months.items():
    if month in val:
        print(key)
