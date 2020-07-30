'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
   Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
print("\nУрок 5 задание 5\n")

import os
import random

dig_str = ''
work_dir = os.path.join(os.path.dirname(__file__), "user_file5.txt")
with open(work_dir, "w", encoding="utf-8") as user_file:
    for _ in range(0, 5):
        dig_str +=  str(random.randint(-10, 10)) + ' '
    user_file.write(dig_str)
    print("Записываем в файл строку чисел: ", dig_str)

with open(work_dir, "r", encoding="utf-8") as user_file:
    str_dig = user_file.read().split(' ')
    file_sum = 0
    for el in str_dig:
        if el == '':
            break
        else:
            file_sum += int(el)
print("Сумма чисел из файла:  ", file_sum)
