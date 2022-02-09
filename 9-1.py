"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""


from time import sleep


class TrafficLight:
    __color = ('red', 'yellow', 'green', 'yellow2')
    __runtime = (7, 2, 3, 2)

    def __init__(self):
        self.color = TrafficLight.__color
        self.runtime = TrafficLight.__runtime
        self.last_color = None

    def color_switching(self):

        for i in range(len(self.color)):
            print(self.color[i])
            self.last_color = self.color[i]
            sleep(self.runtime[i])

    def running(self):

        if self.last_color is not None:

            idx = self.color.index(self.last_color)
            sleep(self.runtime[idx])

            for i in range(idx, len(self.color)):
                print(self.color[i])
                self.last_color = self.color[i]
                sleep(self.runtime[i])

            while True:

                self.color_switching()

        else:

            while True:

                self.color_switching()






if __name__ == '__main__':
    test = TrafficLight()

    test.last_color = 'yellow2'
    test.running()




