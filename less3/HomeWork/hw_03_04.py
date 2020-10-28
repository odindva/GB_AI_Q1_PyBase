# 4) Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def negative_degree(x, y):
    """Возвращает возведение числа x в степень y

    x - действительное положительное число
    y - целое отрицательное число
    Для некорректных аргументов возвращает None"""
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            raise ValueError
    except ValueError:
        return None
    return x ** y


def negative_degree2(x, y):
    """Возвращает возведение числа x в степень y

    x - действительное положительное число
    y - целое отрицательное число
    Для некорректных аргументов возвращает None"""
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            raise ValueError
    except ValueError:
        return None
    result = 1.0
    while y < 0:
        result *= x
        y += 1
    return 1 / result


print(negative_degree(2, -2))
print(negative_degree(-2, -2))
print(negative_degree(-2, 2))
print(negative_degree(-2, -2.5))
print(negative_degree(2.5, -2))
print()
print(negative_degree2(2, -2))
print(negative_degree2(-2, -2))
print(negative_degree2(-2, 2))
print(negative_degree2(-2, -2.5))
print(negative_degree2(2.5, -2))
