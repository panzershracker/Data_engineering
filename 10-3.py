"""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и округление до целого числа деления клеток, соответственно.
Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух.
Число ячеек общей клетки — произведение количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, n_elements):
        self.n_elements = n_elements

    def __add__(self, other):
        return Cell(self.n_elements + other.n_elements)

    def __sub__(self, other):
        if self.n_elements <= other.n_elements:
            print('Кол-во элементов в первой клетке меньше чем во второй или разность нулевая!')
        else:
            return Cell(self.n_elements - other.n_elements)

    def __mul__(self, other):
        return Cell(self.n_elements * other.n_elements)

    def __truediv__(self, other):
        return Cell(self.n_elements // other.n_elements)

    @property
    def n_elements(self):
        return self.__n_elements

    @n_elements.setter
    def n_elements(self, n_elements):
        if n_elements <= 0:
            print('Кол-во элементов не должно быть меньше или равно нулю.')
        self.__n_elements = n_elements

    @n_elements.getter
    def n_elements(self):
        return self.__n_elements

    def make_order(self, row_len):
        assert isinstance(row_len, int) and row_len <= self.n_elements, \
            'Число длинны строки должно быть целым, неотрицательным, менее или равно кол-ву элементов всего.'

        n_int_rows = self.n_elements // row_len
        result = ('o' * row_len + '\n') * n_int_rows
        reminder = 'o' * (self.n_elements - n_int_rows * row_len) + '\n'

        return result + reminder


cell_1 = Cell(20)
cell_2 = Cell(10)

print(f'Cell_1 structure is:\n{cell_1.make_order(5)}')
print(f'Cell_2 structure is:\n{cell_1.make_order(5)}')

cell_3 = cell_1 + cell_2
print(f'addition result is: {cell_3.n_elements}\n')

cell_3 = cell_1 - cell_2
print(f'subtract result is: {cell_3.n_elements}\n')

cell_3 = cell_1 * cell_2
print(f'multiplication result is: {cell_3.n_elements}\n')

cell_3 = cell_1 / cell_2
print(f'division result is: {cell_3.n_elements}\n')






