'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
   Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
   Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
   Результат: [12, 44, 4, 10, 78, 123].
'''
print("\nУрок 4 задание 2\n")

numbers = [] #list()

try:
    user_str = input("Введите строку чисел через запятую\n")
    numbers = user_str.split(',')
    #print('Омма: ', numbers)
except ValueError:
    print('Неверный формат')

#numbers = [300,2,12,44,1,1,4,10,7,1,78,123,55,66,12,8,44]

#gen_list = [numbers[i] for i in range(1,len(numbers)) if int(numbers[i]) > int(numbers[i-1])]

gen_list = [numbers[_] for _ in range(1, len(numbers)) if int(numbers[_]) > int(numbers[_-1])]

print("Введено   : ", numbers)
print("Результат : ", gen_list)
