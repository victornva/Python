'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
   количества слов в каждой строке.
   '''
print("\nУрок 5 задание 2\n")

import os

str_num = 0

work_dir = os.path.join(os.path.dirname(__file__), "user_file2.txt")
with open(work_dir, "r", encoding="utf-8") as user_file:
    while True:
        str = user_file.readline()
        if not str:
            print("\nВсего строк в файле: ", str_num)
            exit()
        else:
            str_num += 1
            print(f"В строке {str_num} кол-во символов {len(str)}")
