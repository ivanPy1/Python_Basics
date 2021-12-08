# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников. 

pay_num = 0
employee_num = 0


with open("lesson-5-hw-3_text.txt", "r") as f:
    print('Список сотрудников с окладом менее 20 тыс.:')

    for line in f:
        list1 = line.split(",")
        surname, pay = list
        pay = int(pay.strip())
        pay_num += pay
        employee_num += 1

        if pay < 20000:
            print(f'Cотрудник (сотрудница) {surname} имеет оклад = {pay}')

if employee_num:
    print(f'Средняя величина дохода сотрудников: {round(pay_num / employee_num, 2)}')
