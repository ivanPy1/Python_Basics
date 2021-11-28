# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_month = int(input('Введите месяц в виде целого числа от 1 до 12 :'))

list_month = ['зима', 'весна', 'лето', 'осень']
dict_month = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

if user_month == 12 or user_month == 1 or user_month == 2:
    print(user_month, 'месяц - это :')
    print(list_month[0])
    print(dict_month.get(1))
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(user_month, 'месяц - это :')
    print(list_month[1])
    print(dict_month.get(2))
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(user_month, 'месяц - это :')
    print(list_month[2])
    print(dict_month.get(3))
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(user_month, 'месяц - это :')
    print(list_month[3])
    print(dict_month.get(4))
else:
    print(user_month, '- такого месяца не существует')
