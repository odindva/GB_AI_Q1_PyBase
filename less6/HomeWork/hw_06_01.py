# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from itertools import cycle
from time import time


class TrafficLight:
    __colors = ('red', 'yellow', 'green')
    __seconds = (7, 2, 7)
    __count_tl = 1

    def __init__(self, color=None):
        self.__color = color if color in TrafficLight.__colors else 'red'
        self.__color_gen = cycle(range(3))
        while True:
            # подгоняет порядок, на основе введенного параметра
            if self.__color == TrafficLight.__colors[next(self.__color_gen)]:
                break
        # нумеруем светофоры (вдруг захотим засунуть в разные потоки)
        self.number = TrafficLight.__count_tl
        TrafficLight.__count_tl += 1

    def print_tl(self):
        print(f'Светофор №{self.number}: {self.__color}')

    def running(self, counts=7, no_limit=False):
        """переключение светофора в режимы: красный, желтый, зеленый

        :param counts: для ограничения итераций
        :param no_limit: для снятия ограничений
        :return:
        """
        self.print_tl()
        t = time()
        while counts > 1:
            if time() - t > TrafficLight.__seconds[TrafficLight.__colors.index(self.__color)]:
                last_color = self.__color
                self.__color = TrafficLight.__colors[next(self.__color_gen)]
                # не представляю возможным вход в эту ветку:
                if last_color != TrafficLight.__colors[TrafficLight.__colors.index(self.__color) - 1]:
                    print('Непонятным образом нарушена последовательность о_О')
                    break
                self.print_tl()
                t = time()
                if not no_limit:
                    counts -= 1


# если время красного и зеленого совпадают
# и если запустить в разных потоках, то это светофоры на перекрестке:
tl_1 = TrafficLight()
tl_1.running()
tl_2 = TrafficLight('green')
tl_2.running(counts=3)

# бесконечный вариант:
# tl_3 = TrafficLight('yellow')
# tl_3.running(no_limit=True)
