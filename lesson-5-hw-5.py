# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму
# чисел в файле и выводить ее на экран.


from random import randint
from functools import reduce

with open("lesson-5-hw-5.txt", "a") as f:
    for i in range(5):
        f.write(str(randint(1, 10)) + " ")

with open("lesson-5-hw-5.txt") as f:
    result = reduce(lambda a, b: a + b, [int(el) for el in [line.split(" ") for line in f][0] if el])
    print(f'Сумма чисел в файле: {result}.')
