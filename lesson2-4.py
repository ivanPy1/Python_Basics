# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите строку из нескольких слов, разделенных пробелами :')
user_word = []
count = 1
for el in range(user_string.count(' ') + 1):
    user_word = user_string.split()
    if len(str(user_word)) <= 10:
        print(f" {count} {user_word [el]}")
        count += 1
    else:
        print(f" {count} {user_word [el] [0:10]}")
        count += 1
