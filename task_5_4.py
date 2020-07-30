'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
	Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
	При этом английские числительные должны заменяться на русские.
	Новый блок строк должен записываться в новый текстовый файл.'''
print("\nУрок 5 задание 4\n")

import os

str_rus = ['Один', 'Два', 'Три', 'Четыре']

src_path = os.path.join(os.path.dirname(__file__), "user_file4_src.txt")
with open(src_path, "r", encoding="utf-8") as src_file:
    str_list = src_file.readlines()

rus_list = []
for str in str_list:
    str_eng = str.split(' ')
    rus_list.append(str_rus[int(str_eng[2])-1] + ' - ' + str_eng[2])

print(rus_list)
dst_path = os.path.join(os.path.dirname(__file__), "user_file4_dst.txt")
with open(dst_path, "w", encoding="utf-8") as dst_file:
    dst_file.writelines(rus_list)