'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
	Значения данных атрибутов должны передаваться при создании экземпляра класса.
	Атрибуты сделать защищенными.
	Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
	Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
	Проверить работу метода.
	Например: 20м * 5000м * 25кг * 5см = 12500 т
'''
print("\nУрок 6 задание 2\n")

class Road:

    _length = 0.0    # длина, м
    _width = 0.0     # ширина, м

    def __init__(self, length, width):
        self._length = length  # плотность 0,01*кг/м3
        self._width = width    # толщина, cм

    def RoadMass(self, density, thickness):
        return self._length * self._width * 0.001*density * thickness

try:
    user_str = input("Введите через запятую длину и ширину дороги, массу асфальта кг/см на 1 кв.м, и толщину полотна в см :\n")
    user_list = user_str.split(',')
    param = [float(item) for item in user_list]
except ValueError:
    exit('Неверный формат')

road_obj = Road(param[0], param[1])

print(f"Длина дороги {road_obj._length} м, ширина {road_obj._width} м, масса 1 кв.м {param[2]} кг/см, толщина полотна {param[3]} см")
print(f"Требуемая масса асфальта: {road_obj.RoadMass(param[2], param[3])} тонн")

