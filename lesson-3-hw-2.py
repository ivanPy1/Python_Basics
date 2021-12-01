# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def user_param(name, surname, year_birth, city, email, number_phone):
    """
    Данная функция принимает параметры, описывающие пользователя: имя, фамилия,
    год рождения, город проживания, email, телефон.
    Выводит полученные данные одной строкой.
    """
    print(
        f' Имя - {name};'
        f' Фамилия - {surname};'
        f' Год рождения - {year_birth};'
        f' Город проживания - {city};'
        f' Email - {email};'
        f' Номер телефона - {number_phone}')


user_param(name='Василий',
           surname='Иванов',
           year_birth='1979',
           city='Москва',
           email='vas_ivanov@mail.ru',
           number_phone='8-999-999-99-99')
