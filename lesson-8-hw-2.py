# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой. 

class DivOnNull:

    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divider_null(dividend, divider):
        try:
            return dividend / divider
        except:
            return f'На ноль делить нельзя'


print(DivOnNull.divider_null(10, 4))
print(DivOnNull.divider_null(10, 0))
print(DivOnNull.divider_null(17, 10))
print(DivOnNull.divider_null(17, 0))
