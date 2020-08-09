'''
4.  Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
    А также класс «Оргтехника», который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов.
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5.  Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
    Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
    можно использовать любую подходящую структуру, например словарь.
6.  Реализуйте механизм валидации вводимых пользователем данных.
'''
print("\nУрок 8 задание 4-5-6\n")

import random
from abc import ABC, abstractmethod

class Store:  #Все переменными сделаем приватными т.к. Главное правило Склада - никто не должен знать что на Складе! (кроме кладовщика)'''

    __goods = dict()   # справочник поступивших на склад позиций
    __map = []         # карта складских ячеек с указанием что там лежит (по ключу)
    __shipped = dict() # книга отгрузки ключ-подразделение-ответственный
    __value = 0        # вместимость, сколько всего мест
    __goods_num = 0    # текущее кол-во занятых мест

    def __init__(self, X, Y):
        '''Класс Склад, X: кол-во полок по горизонтали, Y: кол-во полок по вертикали, __value: вместимость'''
        self.X = X
        self.Y = Y
        self.__value = X * Y
        print(f'Построен склад размером {X}x{Y} ячеек вместимостью {self.__value} мест')
        self.__map = [['|___|' for _ in range(Y)] for __ in range(X)]

    def __str__(self):
        '''метод для отображения схемы заполнения склада'''
        print("\nСхема склада: |___| - свободная ячейка")
        return '\n'.join('   '.join(map(str, _)) for _ in self.__map)

    def recept(self, gkey, prop_list):
        '''Метод для принятия товара на склад'''
        if self.__goods_num < self.__value:  # если на складе есть место...
            while True:                      # выбираем полку в случайном порядке - это чтобы вес распределялся
                x = random.randint(0, self.X - 1)    # более-менее равномерно - если брать первый пустой
                y = random.randint(0, self.Y - 1)    # (допустим с начала) - стелаж перекосит
                if self.__map[x][y] == '|___|':      # если полка свободна - используем, если нет - выбираем другую
                    self.__map[x][y] = gkey          # метим её как занятую - вешаем табличку с ключом
                    self.__goods_num += 1            # увеличиваем кол-во позиций на складе на единицу
                    self.__goods[gkey] = prop_list   # заносим товар в амбарную книгу
                    return [x, y]                    # возвращаем расписку с координатами полки

    def ship(self, place, dep, resp):
        '''Метод отгрузки товара со склада: в его свойствах уже есть коорд. полки'''
        self.__shipped[self.__map[place[0]][place[1]]] = [dep, resp]  # заносим товар в книгу отгрузки
        self.__map[place[0]][place[1]] = '|___|'  # освобождаем полку
        self.__goods_num -= 1  # уменьшаем кол-во позиций на складе на единицу

    def find(self, gkey):
        '''метод для проверки наличия товара с данным ключом на складе'''
        for row in self.__map:
            for el in row:
                if el == gkey:
                    return True
        return False

    @property
    def free(self):
        '''метод для отображения кол-ва свободных мест склада'''
        return self.__value - self.__goods_num

    def goods_view(self):
        '''метод для отображения списка принятых товаров'''
        for key in self.__goods.keys():
            print(f'Принято: идентификатор - {key} - параметры {self.__goods[key]}')

    def shipped_view(self):
        '''метод для отображения списка отгруженных (выданных) товаров'''
        for key in self.__shipped.keys():
            print(f'Выдано : идентификатор - {key} - параметры {self.__shipped[key]}')

    def goods_validate(self, gkey):
        '''метод для проверки идентификатора товара в справочнике'''
        for key in self.__goods.keys():
            if key == gkey:
                return True
        return False

    def ship_validate(self, gkey):
        '''метод для проверки идентификатора товара в отгруженных'''
        for key in self.__shipped.keys():
            if key == gkey:
                print(f'Позиция {gkey} отгружена: {self.__shipped[gkey]}')
                return True
        return False

#------------------------------------------------------------------------------------------------------------
class Equip:
    '''Класс оборудования'''
    type = ''
    desc = ''
    price = 0.0
    place = []

class Printer(Equip):
    type = 'Принтер'
    mfp = False
    lan = False
    color = False

    def __init__(self, param_list):
        self.desc = param_list[0]
        self.price = param_list[1]
        self.mfp = param_list[2]
        self.lan = param_list[3]
        self.color = param_list[4]
        print(f'{self.type}: {self.desc}, МФУ-{self.mfp} Сеть-{self.lan} Цвет {self.color} цена {self.price}')

class Computer(Equip):
    type = 'Компьютер'
    os_type = None
    notebook = False

    def __init__(self, param_list):
        self.desc = param_list[0]
        self.price = param_list[1]
        self.os_type = param_list[2]
        self.notebook = param_list[3]
        print(f'{self.type}: {self.desc}, ОС-{self.os_type} Ноут-{self.notebook} цена {self.price}')

class Server(Equip):
    type = 'Сервер'
    os_type = None
    cpu_num = 0
    disk_num = 0
    lan_num = 0

    def __init__(self, param_list):
        self.desc = param_list[0]
        self.price = param_list[1]
        self.os_type = param_list[2]
        self.cpu_num = param_list[3]
        self.disk_num = param_list[4]
        self.lan_num = param_list[5]
        print(f'{self.type}: {self.desc}, ОС-{self.os_type} CPUx{self.cpu_num} Disk-{self.disk_num} LANx{self.lan_num} цена {self.price}')

class DigEx(Exception):

    def __init__(self):
        print('Это не число')

#------------------------------------------------------------------------------------------------------------
#
# Создадим объект склад
a = Store(4, 5)

print('\nНачнём ввод данных - предварительно зададим несколько позиций:\n')
prn1 = Printer(['HP526', 35000, True, True, False])
comp1 = Computer(['Dell Latitude', 55000, 'Win10Pro', True])
srv1 = Server(['Dell R640', 1550000, 'WinServer2019', 2, 6, 4])

print('\nИ примем их на наш склад: ')
print('\nСвободных мест: ', a.free)
comp1.place = a.recept('comp1', ['Dell Latitude', 55000, 'Win10Pro', True])
print(f'Место на складе для {comp1.desc}: ', comp1.place)
srv1.place = a.recept('srv1', [srv1.desc, srv1.price, srv1.os_type, srv1.cpu_num, srv1.disk_num, srv1.lan_num])
print(f'Место на складе для {srv1.desc}: ', srv1.place)
prn1.place = a.recept('prn1', ['HP526', 35000, True, True, False])
print(f'Место на складе для {prn1.desc}: ', prn1.place)
print('\nСвободных мест: ', a.free)

print('\nСмотрим справочник поступивших товаров:')
print(a.goods_view())
print('\nи размещение их на складе:')
print(a)

print('\nТеперь будем вводить поступления на склад с клавиатуры')
print('\nВвод такого рода информации с клавиатуры в консоли программы - плохой и громоздкий вариант из далёкого прошлого...')
print('... но для примера сделаем, для компьютера')
while True:
    try:
        new_eq = input("Введите идентификатор оборудования или q для выхода:\n")
        if new_eq == 'q':
            break
        if a.goods_validate(new_eq) == True: # проверка идентификатора
            print('Такой идентификатор уже имеется, введите другой')
        else:
            #eq_type = input("Введите тип оборудования: s - сервер, c - компьютер, p - принтер:\n")
            comp_name = input("Введите название компьютера:\n")
            comp_price = input("Введите цену компьютера:\n")
            if comp_price.isdigit() == False: # если введено не число - поднимаем исключение
                raise DigEx()
            comp_os = input("Введите название ОС:\n")
            comp_notebook = input("Это ноутбук? (Y/n):\n")
            if comp_notebook.lower() == 'y':
                answ = True
            else:
                answ = False
            # создаём объект товара и запускаем метод нашего склада для его добавления на склад
            Computer([comp_name, float(comp_price), comp_os, answ])
            a.recept(new_eq, [comp_name, float(comp_price), comp_os, answ])
            print(a)
    except DigEx as err:
        print('Ошибка ')

print('Свободных мест: ', a.free)
print(a)

# Отгрузка
print('\nТеперь выдадим оборудование со склада в какое-нибудь подразделение (для демонстрации не будем заморачиваться с клавиатурным вводом):\n')

print('Проверяем есть ли на складе запрошенная по идентификатору позиция, и если есть отгружаем:')
if a.find('prn1') == True:
    a.ship(prn1.place, 'Бухгалтерия', 'Иванова')
    print('prn1 отгружен? ', a.ship_validate('prn1'))
    print(a)
    print('Свободных мест: ', a.free)

if a.find('comp1') == True:
    a.ship(comp1.place, 'Юр.отдел', 'Петров')
    print('comp1 отгружен? ', a.ship_validate('comp1'))
    print(a)
    print('Свободных мест: ', a.free)

print('\nСмотрим список отгруженного оборудования:')
print(a.shipped_view())

print('\nСмотрим список оборудования прошедшего через склад:')
print(a.goods_view())
