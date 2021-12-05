# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv 


def pay_employ(hours, ret_per_hour, bonus):
    """
    Данная функция расчитывает заработную плату сотрудника
    """
    payment = (hours * ret_per_hour) + bonus
    print(f'Заработная плата сотрудника {payment}')


script_name, hours, ret_per_hour, bonus = argv

hours = int(hours)
ret_per_hour = int(ret_per_hour)
bonus = int(bonus)

print('Имя скрипта: ', script_name)
print('Выработка в часах: ', hours)
print('Ставка в час: ', ret_per_hour)
print('Премия: ', bonus)

pay_employ(hours, ret_per_hour, bonus)
