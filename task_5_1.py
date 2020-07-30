'''
1.  Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
	   Об окончании ввода данных свидетельствует пустая строка.
'''
print("\nУрок 5 задание 1\n")

import os

user_list = []

while True:
    try:
        user_str = str(input("Введите строку\n"))
        if user_str == '':
            print('Пока!')
            break
        else:
            user_list.append(user_str + "\n")
    except ValueError:
        print('Неверный формат')

work_dir = os.path.join(os.path.dirname(__file__), "user_file1.txt")
user_file = open(work_dir, "a", encoding="utf-8")
user_file.writelines(user_list)
user_file.close()