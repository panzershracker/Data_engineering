"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;

создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title} начал отрисовку')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} начал отрисовку')


class Marker(Stationery):

    def draw(self):
        print(f'{self.title} начал отрисовку')


pen, pencil, marker = Pen('pen'), Pencil('pencil'), Marker('marker')

print(pen.title)
pen.draw()
print('\n')

print(pencil.title)
pencil.draw()
print('\n')

print(marker.title)
marker.draw()
