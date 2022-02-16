"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:

    def __init__(self, str_num):
        self.num = complex(str_num)

    def __add__(self, other):
        return ComplexNum(self.num + other.num)

    def __mul__(self, other):
        return ComplexNum(self.num * other.num)


test_1 = ComplexNum('1+2j')
test_2 = ComplexNum('2+2j')

addition = test_1 + test_2
multiplication = test_1 * test_2

print(f'Addition result is: {addition.num}, {type(addition.num)}')
print(f'Multiplication result is: {multiplication.num}, {type(multiplication.num)}')