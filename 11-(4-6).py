"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""

import random


class WareHouse:
    __total_quantity = 0
    __scanners_quantity = 0
    __printers_quantity = 0
    __locations = ('warehouse', 'office', 'reception')
    __id_locs = {}

    """Не использую декораторы геттеров и сеттеров, т.к. иначе придется привязывать счетчики 
    к отдельным экземплярам (инстансам) класса через конструктор/инициализатор __init__"""

    @classmethod
    def get_total(cls):
        """Общее кол-во орг техники"""

        return cls.__total_quantity

    @classmethod
    def get_scanners(cls):
        """Общее кол-во сканеров"""

        return cls.__scanners_quantity

    @classmethod
    def get_printers(cls):
        """Общее кол-во принтеров"""

        return cls.__printers_quantity

    @classmethod
    def set_scanners(cls):
        """Инкремент кол-ва сканеров"""

        cls.__scanners_quantity += 1
        cls.__total_quantity += 1

    @classmethod
    def set_printers(cls):
        """Инкремент кол-вап принтеров"""

        cls.__printers_quantity += 1
        cls.__total_quantity += 1

    @classmethod
    def id_locs_fill(cls, id):
        """Дефолтное значение местоположения
        (сначала вся техника ппоступает на склад, а затем ее можно переместить)"""

        cls.__id_locs[id] = 'warehouse'

    @classmethod
    def random_locs_fill(cls, id):
        """Альтернативный метод присвоения местоположения для техники (для генератора инстансов)"""

        cls.__id_locs[id] = random.choice(cls.__locations)

    @classmethod
    def find_item(cls, id=None, dep=None):
        """Поиск подразделения где находится техника с id, или перечень всех id в подразделении."""

        if id:
            return cls.__id_locs[id]
        elif dep:
            return [k for k, v in cls.__id_locs.items() if v == dep]
        else:
            print('Такого id не существет, или неверно указан департамент.')

    @classmethod
    def move_to_department(cls, id, destination):
        """Перемещение из текущего подразделения в новое"""

        if id in cls.__id_locs.keys() and destination != cls.find_item(id):
            print(f'Техника с ID = {id} перемещена из {cls.__id_locs[id]} в {destination}')
            cls.__id_locs[id] = destination

        else:
            print('ID не существует, либо он уже находится в данном подразделении')

    @classmethod
    def items_per_department(cls, department):
        """Всего единиц техники на подразделение"""

        if department in cls.__locations:
            return sum([k for k, v in cls.__id_locs if v == department])
        else:
            print('Такого подразделения не существет, воспользуйтесь .show_departments()')

    @classmethod
    def show_departments(cls):
        """Выводит список подразделений"""

        return cls.__locations


class OfficeEquipment:

    def __init__(self, color, size, id, loc='default'):
        self.color = color
        self.size = size
        self.id = id
        if loc == 'default':
            WareHouse.id_locs_fill(id)
        elif loc in WareHouse.show_departments():
            WareHouse.random_locs_fill(id)
        else:
            print('Такого департамента нет. Воспользуйся WareHouse.show_departments()')


class Scanner(OfficeEquipment):

    def __init__(self, color, size, dpi, id, loc):
        super().__init__(color, size, id, loc)
        self.dpi = dpi

        WareHouse.set_scanners()

    @staticmethod
    def action():
        print('Сканер сканирует')


class Printer(OfficeEquipment):

    def __init__(self, color, size, type, id, loc):
        super().__init__(color, size, id, loc)
        self.type = type

        WareHouse.set_printers()

    @staticmethod
    def action():
        print('Принтер печатает')


def populator(n_scanners, n_printers):
    """Автомарически генерируем необходимое кол-во инстансов каждой категории"""

    colors = ('white', 'black')
    sizes = ('small', 'medium', 'large')
    types = ('laser', 'jet')
    dpis = (1024, 2048, 4096)
    locations = ('warehouse', 'office', 'reception')

    for i in range(1, n_scanners + 1):
        globals()[f"scanner_{i}"] = Scanner(random.choice(colors),
                                            random.choice(sizes),
                                            random.choice(dpis),
                                            i,
                                            random.choice(locations))

    for i in range(1, n_printers + 1):
        globals()[f"printer_{i}"] = Printer(random.choice(colors),
                                            random.choice(sizes),
                                            random.choice(types),
                                            n_scanners + i,
                                            loc=random.choice(locations))

    return 'done'

warehouse = WareHouse
pop = populator(2, 2)


print('---Вывод атрибутов разных инстансов для проверки корректности их создания---')
print(scanner_1.dpi)
print(scanner_2.color)
print(printer_1.type)
print(printer_2.size)

print('\n---Подстчет техники---')
print(f'Printers count = {warehouse.get_printers()}, '
      f'scanners count = {warehouse.get_scanners()}, '
      f'items total = {warehouse.get_total()}')

print('\n---Перемещение между подразделениями---')
warehouse.move_to_department(1, 'office')

print('\n---Поиск по id и названию подразделения')
print(f'Подразделение в котором находится указанный id = {warehouse.find_item(id=4)}')
print(f'Список id находящихся в указанном подразделении: {warehouse.find_item(dep="office")}')