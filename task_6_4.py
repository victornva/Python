'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
   А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
   Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
   Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
   Для классов TownCar и WorkCar переопределите метод show_speed.
   При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
   Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
   Выполните вызов методов и также покажите результат.
'''
print("\nУрок 6 задание 4\n")

class Car:
    name = 'Car'
    color = ''
    speed = 0.0
    is_police = False

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'\nМашина {self.name} цвета {self.color} выехала!')

    def go(self, speed):
        self.speed = speed
        print(f'машина {self.name} поехала со скоростью {self.speed}')

    def stop(self):
        self.speed = 0.0
        print(f'машина {self.name} остановилась')

    def turn(self, direction): print(f'машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'скорость {self.speed}')
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'машина {self.name} скорость {self.speed} !!Превышена!!')
        else:
            print(f'машина {self.name} скорость {self.speed}')
        return self.speed

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'машина {self.name} скорость {self.speed} !!Превышена!!')
        else:
            print(f'машина {self.name} скорость {self.speed}')
        return self.speed

class PoliceCar(Car):
    pass


# Выпускаем Линкольн Таун Кар!
Lincoln = TownCar('Lincoln', 'White', 0.0, False)
print('Это полицейска машина? ', Lincoln.is_police)
Lincoln.go(50)
Lincoln.go(70)
Lincoln.show_speed()
Lincoln.go(60)
Lincoln.turn('направо')
Lincoln.stop()
Lincoln.show_speed()

# Выпускаем полицейскую Шевроле Импала Police !
Impala = PoliceCar('Impala', 'Black&White', 0, True)
print('Это полицейска машина? ', Impala.is_police)
Impala.go(50)
Impala.go(150)
Impala.show_speed()
Impala.turn('назад')
Impala.stop()
Impala.show_speed()

# Выпускаем Форд Мустанг !
Mustang = SportCar('Mustang', 'Red', 0, False)
print('Это полицейска машина? ', Mustang.is_police)
Mustang.go(50)
Mustang.go(200)
Mustang.show_speed()
Mustang.turn('налево')
Mustang.show_speed()
Mustang.go(100)
Mustang.show_speed()
Mustang.stop()
Mustang.show_speed()

# Выпускаем грузовой Frighliner !
Frighliner = WorkCar('Frighliner', 'Blue', 0, False)
print('Это полицейска машина? ', Frighliner.is_police)
Frighliner.go(30)
Frighliner.go(100)
Frighliner.show_speed()
Frighliner.turn('налево')
Frighliner.show_speed()
Frighliner.go(40)
Frighliner.show_speed()
Frighliner.stop()
Frighliner.show_speed()
