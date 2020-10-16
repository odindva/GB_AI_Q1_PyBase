# 5) Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


# import time
from functools import reduce

# t = time.time()

print(reduce(lambda x, y: x * y, [i for i in range(100, 1001) if not i & 1]))
# print(len(str(reduce(lambda x, y: x * y, [i for i in range(100, 1001) if not i & 1]))), '- значное число')
# print(time.time() - t)
#
#
# t = time.time()
# p = 1
# for i in range(100, 1001):
#     if not i & 1:
#         p *= i
# print(p)
# print(time.time() - t)

# Решил проверить время выполнения, но в этой задаче нет проигравшего )
# даже при range(100, 100001)
