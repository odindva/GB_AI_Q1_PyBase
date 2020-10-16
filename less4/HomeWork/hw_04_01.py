# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv


def help_me():
    print('скрипт принимает от 2 до 3 параметров\n'
          'расчитывает заработную плату сотрудника\n'
          'первый параметр - выработка в часах\n'
          'второй параметр - ставка\n'
          'третий параметр - премия (по умолчанию равна 0)\n'
          'последующие параметры игнорируются')


def payroll(production_in_hours, rate_per_hour, award='0'):
    """Возвращает расчетную зарплату или None при некорректных данных

    :param production_in_hours: выработка в часах
    :param rate_per_hour: ставка в час
    :param award: премия
    :return: (выработка в часах*ставка в час) + премия
    """
    try:
        production_in_hours = float(production_in_hours)
        rate_per_hour = float(rate_per_hour)
        award = float(award)
    except ValueError:
        return 'Скрипт принимает 3 числовых параметра'
    else:
        return production_in_hours * rate_per_hour + award


try:
    if len(argv) == 3:
        print(payroll(production_in_hours=argv[1], rate_per_hour=argv[2]))
    else:
        print(payroll(production_in_hours=argv[1], rate_per_hour=argv[2], award=argv[3]))
except IndexError:
    help_me()
