# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division_a_by_b(dividend, divider):
    """Вернет частное от деления a на b

    Если b = 0 вернет None
    """
    return dividend / divider if divider != 0 else None


while True:
    try:
        a = int(input('Введите делимое: '))
        break
    except ValueError:
        print('Введено не число')
while True:
    try:
        b = int(input('Введите делитель: '))
        if b == 0:
            raise ZeroDivisionError  # Проверка деления на 0 в рамках дружелюбного интерфейса
        break
    except ValueError:
        print('Введено не число')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
print(division_a_by_b(a, b))
