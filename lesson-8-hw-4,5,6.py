# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.


class OfficeEquipmentWarehouse:

    def __init__(self, name, price, amount, num_list, *args):
        self.name = name
        self.price = price
        self.amount = amount
        self.numb = num_list
        self.store_total = []
        self.store= []
        self.module = {'Модель оргтехники': self.name, 'Цена за ед': self.price, 'Количество': self.amount}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.amount}'


    def recip(self):
        try:
            unit = input(f'Введите название товара ')
            unit_p = int(input(f'Введите цену за единицу продукции '))
            unit_q = int(input(f'Введите количество товара'))
            unique = {'Модель устройства': unit, 'Цена за единицу продукции': unit_p, 'Количество товара': unit_q}
            self.module.update(unique)
            self.store.append(self.module)
            print(f'Текущий список -\n {self.store}')
        except:
            return f'Ошибка ввода данных'

        active = input(f'Для выхода введите Q, для продолжения - Enter') 
        if active == 'Q':
            self.store_total.append(self.store)
            print(f'Весь склад -\n {self.store_total}')
            return f'Выход'
        else:
            return OfficeEquipmentWarehouse.recip(self)


class Printer(OfficeEquipmentWarehouse):
    def to_print(self):
        return f'{self.numb}'


class Scanner(OfficeEquipmentWarehouse):
    def to_scan(self):
        return f'{self.numb}'


class Copier(OfficeEquipmentWarehouse):
    def to_copier(self):
        return f'{self.numb}'


unit_1 = Printer('Epson', 3000, 10, 5)
unit_2 = Scanner('HP', 1700, 5, 15)
unit_3 = Copier('Panasonic', 5000, 1, 10)
print(unit_1.recip())
print(unit_2.recip())
print(unit_3.recip())
print(unit_1.to_print())
print(unit_3.to_copier())
