# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return print(f'z1 + z2 = {self.a + other.a} + {self.b + other.b} * i')

    def __mul__(self, other):
        return print(
            f'z1 * z2 = {self.a * other.a - (self.b * other.b)} + {self.a * other.b + (self.b * other.a)} * i')


z1 = ComplexNumber(5, 7) 
z2 = ComplexNumber(-6, 9)

print(z1 + z2)
print(z1 * z2)
 