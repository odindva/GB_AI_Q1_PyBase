# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    """Возвращает сумму наибольших двух аргументов

    Принимает три числа,
    для некорректных аргументов возвращает None"""
    try:
        arr = [int(arg1), int(arg2), int(arg3)]
    except ValueError:
        return None
    arr.remove(min(arr))
    return sum(arr)


print(my_func(1, '2', 3))
