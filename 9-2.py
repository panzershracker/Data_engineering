"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness

    def asphalt_weight_calc(self):

        result = self._length * self._width * 25 * self._thickness

        return result / 1000


road_test = Road(5000, 20, 5)
total_weight = road_test.asphalt_weight_calc()

print(total_weight)
# out: 12500.0

