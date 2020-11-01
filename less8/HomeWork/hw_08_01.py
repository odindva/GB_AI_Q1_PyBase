# 1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.__invalid = False
        self._date = date
        try:
            self._date = Date.to_int(date)
        except ValueError:
            self.__invalid = True
            del self
        else:
            if not Date.valid(self._date):
                self.__invalid = True
                del self

    def __del__(self):
        if self.__invalid:
            print(f'{self._date} - is invalid date. Deleted')

    def __str__(self):
        return '' if self.__invalid else f'\nDate: {self._date[0]:02}.{self._date[1]:02}.{self._date[2]:04}'

    @classmethod
    def to_int(cls, date):
        return [int(i) for i in date.split('-')]

    @staticmethod
    def valid(date):
        if not 0 < date[0] < 32:
            return False
        elif not 0 < date[1] < 13:
            return False
        elif not 0 < date[2]:
            return False
        return True


if __name__ == '__main__':
    print(Date('111-12-2020'))
    print(Date('1-2-2030'))
    print(Date('1-13-2020'))
    print(Date('1-1f3-2020'))
