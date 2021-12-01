# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = [14.3, 'Python', 12, False]
print(my_list)
print(my_list[0], type(my_list[0]))
print(my_list[1], type(my_list[1]))
print(my_list[2], type(my_list[2]))
print(my_list[3], type(my_list[3]))

print('-------или через цикл for c использованием type-------:')

for el in range(len(my_list)):
    print(my_list[el], type(my_list[el]))
