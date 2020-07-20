''' 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
       и возвращает сумму наибольших двух аргументов.'''

print("\nУрок 3 задание 3\n")

# складываем все 3 числа и вычитаем из суммы наименьшее
def max_sum2_func(a1, a2, a3):
    '''
    Максимальная сумма 2х чисел из 3х
    :param a1: int,float
    :param a2: int,float
    :param a3: int,float
    :return: int,float, макс.сумма 2х аргументов
    '''
    return a1 + a2 + a3 - min_iter_func([a1, a2, a3])

def min_iter_func(iter_arg):
    '''
    ф-ция возвращает минимальное значение итерируемого объекта
    :param iter_arg: итерируемый объект состоящий из чисел
    :return: элемент с минимальным значением
    '''
    min = iter_arg[0]
    for dig in iter_arg:
        if min > dig:
            min = dig
    return min

try:
    num_1 = float(input("Введите 1-е число\n"))
    num_2 = float(input("Введите 2-е число\n"))
    num_3 = float(input("Введите 3-е число\n"))
except ValueError:
    print('Неверный формат')
    exit()

print("Сумма наибольших двух аргументов: ", max_sum2_func(num_1, num_2, num_3))
