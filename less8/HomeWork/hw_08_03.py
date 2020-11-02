# 3) Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные
# и заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.


class Invalid(Exception):
    def __init__(self, text):
        self.txt = text


nums = []
while True:
    string = input('input number: ')
    if string == 'stop':
        break
    try:
        for i in range(len(string)):
            if i == 0 and (string[i] == '-' or string[i] == '+'):
                continue
            if not string[i].isdigit():
                raise Invalid("it's not number")
    except Invalid as err:
        print(err)
    else:
        nums.append(int(string))
print(nums)
