'''1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
print("\nУрок 7 задание 1\n")

class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        #return str(self.data)
        return '\n'.join(' '.join(map(str, _)) for _ in self.data)

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError('Сложение невозможно т.к. размерность матриц не совпадает')
        summ = []
        row_num = len(self.data)
        col_num = len(self.data[0])
        i = 0
        while i < row_num:
            j = 0
            new_row = []
            while j < col_num:
                new_el = self.data[i][j] + other.data[i][j]
                new_row.append(new_el)
                j += 1
            summ.append(new_row)
            i += 1
        return Matrix(summ)

a = Matrix([[1,2,3], [4,5,6], [7,8,9]])
b = Matrix([[10,11,12], [13,14,15], [16,17,18]])

print('матрица а:')
print(a)
print('\nматрица b:')
print(b)
neo = a+b
print('\nих сумма:')
print(neo)