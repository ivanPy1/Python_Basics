# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
 
dict_translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open("lesson-5-hw-4_text_eng.txt", "r") as f:
    num_list = [line.split(" - ") for line in f]
    num_list = [[dict_translate[el[0]], el[1]] for el in num_list]

with open("lesson-5-hw-4_text_ru.txt", "w") as f:
    [f.write(f'{el[0]} — {el[1]}') for el in num_list]
