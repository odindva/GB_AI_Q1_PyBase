# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from random import choice
from tkinter import Tk, Canvas
import threading
from itertools import cycle
from time import sleep


class TrafficLight:
    __colors = ('red', 'yellow_r_g', 'green', 'yellow_g_r')
    __seconds = (3, 2, 3, 2)
    __count_tl = 1

    def __init__(self, color=None, diam=200):
        self.__color = color if color in TrafficLight.__colors else 'red'
        self.__color_gen = cycle(range(len(TrafficLight.__colors)))
        while True:
            # подгоняет порядок, на основе введенного параметра
            if self.__color == TrafficLight.__colors[next(self.__color_gen)]:
                break
        # нумеруем светофоры (вдруг, захотим запускать в разных потоках)
        self.number = TrafficLight.__count_tl
        self.diam = diam
        TrafficLight.__count_tl += 1

        self.window = Tk()
        self.window.title(f'№{self.number}')
        self.canvas = Canvas(self.window, width=diam, height=diam * 3)
        self.canvas.pack()

    def show_tl(self):
        """Отображение работы светофора

        :return: Выводит в окно результат
        """
        # заполняем серым весь светофор
        for i in range(3):
            self.canvas.create_oval(0, i * self.diam, self.diam, (i + 1) * self.diam, fill='grey')

        # устанавливаем нужный цвет
        if self.__color == TrafficLight.__colors[0]:
            self.canvas.create_oval(0, 0 * self.diam, self.diam, 1 * self.diam, fill='red')
        elif self.__color == TrafficLight.__colors[1]:
            self.canvas.create_oval(0, 0 * self.diam, self.diam, 1 * self.diam, fill='red')
            self.canvas.create_oval(0, 1 * self.diam, self.diam, 2 * self.diam, fill='yellow')
        elif self.__color == TrafficLight.__colors[2]:
            self.canvas.create_oval(0, 2 * self.diam, self.diam, 3 * self.diam, fill='green')
        elif self.__color == TrafficLight.__colors[3]:
            self.canvas.create_oval(0, 1 * self.diam, self.diam, 2 * self.diam, fill='yellow')

        # обновление окна
        self.window.update()

        # консольный вывод:
        # print(f'Светофор №{self.number}: {self.__color}')

    def running(self, counts=10, limit=True):
        """переключение светофора в режимы: красный, желтый, зеленый

        :param counts: для ограничения итераций
        :param limit: для снятия ограничений
        :return:
        """
        self.show_tl()
        while counts > 1:
            last_color = self.__color
            self.__color = TrafficLight.__colors[next(self.__color_gen)]

            # Проверка на неверный порядок. Не представляю возможным вход в эту ветку:
            if last_color != TrafficLight.__colors[TrafficLight.__colors.index(self.__color) - 1]:
                print('Непонятным образом нарушена последовательность о_О')
                break

            # Задержка во времени
            sleep(TrafficLight.__seconds[TrafficLight.__colors.index(self.__color)])
            self.show_tl()

            # По умолчанию есть ограничение цикла
            if limit:
                counts -= 1


tl_1 = TrafficLight()
tl_2 = TrafficLight('green')
threading.Thread(target=tl_1.running()).start()
threading.Thread(target=tl_2.running()).start()

# бесконечный вариант:
# tl_3 = TrafficLight('yellow')
# tl_3.running(no_limit=False)
