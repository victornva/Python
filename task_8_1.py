'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
   В рамках класса реализовать два метода.
   Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
   Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
   Проверить работу полученной структуры на реальных данных.
'''
print("\nУрок 8 задание 1\n")

from datetime import datetime

class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def parser(cls, date_str):
        data = datetime.date(datetime.strptime(date_str, '%d-%m-%Y'))
        return [data.day, data.month, data.year]

    @staticmethod
    def validator(date_str):
        try:
            datetime.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            raise ValueError("Неправильный формат даты день-месяц-год, или такой даты не может существовать")
            #return False
        else:
            print(f'Формат даты {date_str} правильный')
            return True
#------------------------------------------------------------------------------------------------------------

my_date = Date('05-08-2020')

# вызываем метод через название класса
int_date = Date.parser('05-08-2020')
print(f'\nДата: число {int_date[0]} месяц {int_date[1]} год {int_date[2]}\n')

# проверяем корректоность даты
Date.validator('05-08-2020')

# проверяем корректоность даты - программа выбрасывает исключение
Date.validator('33-08-2020')

#assert Date.validator('08-08-2020') # корректная дата
#assert Date.validator('31-08-2020') # НЕкорректная дата