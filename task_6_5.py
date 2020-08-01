'''
5.  Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка).
    Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
print("\nУрок 6 задание 5\n")

class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск ручки')

class Pencil(Stationery):
    def draw(self):
        print('Запуск карандаша')

class Handle(Stationery):
    def draw(self):
        print('Запуск маркера')


s = Stationery('Канцелярия')
print(s.title)
s.draw()

p = Pen('Ручка')
print(p.title)
p.draw()

c = Pencil('Карандаш')
print(c.title)
c.draw()

h = Pencil('Маркер')
print(h.title)
h.draw()
