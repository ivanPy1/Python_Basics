# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import randint 


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_poliсe = is_police

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        self.direction = {1: "налево", 2: "направо"}
        print(f'Машина повернула {self.direction[direction]}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} - превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} - превышение скорости')


class PoliceCar(Car):
    pass


car_list = [TownCar(70, 'белый', 'Skoda', False), SportCar(160, 'красный', 'Ferrari', False),
            WorkCar(60, 'серый', 'ЗИЛ-130', False), PoliceCar(100, 'голубой', 'Nissan', True)]

for el in car_list:
    print(f'Модель машины - {el.name}')
    print(f'Цвет машины - {el.color}')
    el.show_speed()
    if el.is_poliсe: print(f'Это полицейский автомобиль')
    el.turn(randint(1, 2))
    el.stop()
    print('-' * 20)
