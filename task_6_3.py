'''
3.  Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''
print("\nУрок 6 задание 3\n")

class Worker:
    name = 'Name'
    surname = 'Surname'
    position = 'Position'
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        #print(self._income)
        return self._income['wage'] + self._income['bonus']

emp1 = Position('Акакий', 'Зинбернштерн','Генеральный директор', {'wage': 100000, 'bonus': 80000})
emp2 = Position('Василий', 'Пупкин','Советник ген.директора', {'wage': 500000, 'bonus': 499000})
emp3 = Position('Вольдемар', 'Сидоров','Гл.бухгалтер', {'wage': 30000, 'bonus': 140000})
emp4 = Position('Василий', 'Мусин-Пушкин','Сторож', {'wage': 5000, 'bonus': 20000})

print('Протокол судебного заседания по Делу №777 об отмывании ден.средств.\nВ ОАО "Развитие" трудились:\n')
print(f'{emp1.get_full_name()} в должности {emp1.position} и суммарным доходом {emp1.get_total_income()} р/мес')
print(f'{emp2.get_full_name()} в должности {emp2.position} и суммарным доходом {emp2.get_total_income()} р/мес')
print(f'{emp3.get_full_name()} в должности {emp3.position} и суммарным доходом {emp3.get_total_income()} р/мес')
print(f'{emp4.get_full_name()} в должности {emp4.position} и суммарным доходом {emp4.get_total_income()} р/мес')
print('\nа также какое-то число остальных сотрудников, для следствия интереса не представляющих...')
