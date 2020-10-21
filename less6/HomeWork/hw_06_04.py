# 4) Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, name, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self, direction):
        print(f'{self.name} turn on {direction}')

    def show_speed(self):
        print(f"{self.name}'s speed - {self.speed}")


class TownCar(Car):
    def show_speed(self):
        restriction = 60
        print(f"{self.name}'s speed - {self.speed}")
        if int(self.speed) > restriction:
            print(f"{self.name} exceeded speed by {int(self.speed) - restriction}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        restriction = 40
        print(f"{self.name}'s speed - {self.speed}")
        if int(self.speed) > restriction:
            print(f"{self.name} exceeded speed by {int(self.speed) - restriction}")


class PoliceCar(Car):
    pass


town_car = TownCar('1', 65, 'red', False)
town_car.go()
town_car.turn(90)
town_car.show_speed()
town_car.stop()
sportCar = SportCar('2', 165, 'blue', False)
sportCar.go()
sportCar.turn(90)
sportCar.show_speed()
sportCar.stop()
