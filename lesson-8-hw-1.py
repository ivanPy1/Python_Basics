# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных. 

class Date:

    def __int__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []
        for i in day_month_year.split():
            if i != '-':
                date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            print('Корректный день')
        else:
            print('День указан неверно')
        if 1 <= month <= 12:
            print('Корректный месяц')
        else:
            print('Месяц указан неверно')
        if 0 < year <= 2022:
            print('Корректный год')
        else:
            print('Год указан неверно')

    def __str__(self):
        return f'Указанная дата {Date.extract(self.day_month_year)} '

print(Date.extract("15-02-2020"))
print(Date.validation(10, 13, 3000))
