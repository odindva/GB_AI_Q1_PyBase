# 5) Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}. drawing')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}. Pen drawing')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}. Pencil drawing')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}. Handle drawing')


st = Stationery('one')
st.draw()
pen = Pen('two')
pen.draw()
pencil = Pencil('three')
pencil.draw()
handle = Handle('four')
handle.draw()
