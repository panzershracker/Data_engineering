"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);

опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;

добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


import random


class Car:

    def __init__(self, max_speed, color, name, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.max_speed = max_speed


    def go(self):
        print(f'Машина {self.name} Поехала.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self):
        direction = random.choice(('лево', 'право'))
        print(f'Машина {self.name} повернула на {direction}')

    def show_speed(self):
        current_speed = random.randint(1, self.max_speed)
        print(f'Текущая скорость {self.name} = {current_speed}')


class TownCar(Car):

    def __init__(self, max_speed, color, name, speed_limit, is_police=False):

        super().__init__(max_speed, color, name, is_police)
        self.speed_limit = speed_limit

    def show_speed(self):
        current_speed = random.randint(1, self.max_speed)

        if current_speed <= self.speed_limit:
            print(f'Текущая скорость {self.name} = {current_speed}')

        else:
            print(f'Скорость {self.name} превышена ({current_speed}), допустимый лимит = {self.speed_limit}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def __init__(self, max_speed, color, name, speed_limit, is_police=False):

        super().__init__(max_speed, color, name, is_police)
        self.speed_limit = speed_limit

    def show_speed(self):
        current_speed = random.randint(1, self.max_speed)

        if current_speed <= self.speed_limit:
            print(f'Текущая скорость {self.name} = {current_speed}')

        else:
            print(f'Скорость {self.name} превышена ({current_speed}), допустимый лимит = {self.speed_limit}')


class PoliceCar(Car):
    pass


town_test = TownCar(100, 'red', 'van', 60)
town_test.go()
town_test.show_speed()
town_test.turn()
town_test.stop()
print('\n')

work_test = WorkCar(80, 'brown', 'pickup', 40)
work_test.go()
work_test.show_speed()
work_test.turn()
work_test.stop()
print('\n')


police_test = PoliceCar(120, 'black', 'hatchback', is_police=True)
print(f'is police = {police_test.is_police}')
police_test.go()
police_test.turn()
police_test.show_speed()
police_test.stop()

