'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
   Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
   Выполнить подсчет средней величины дохода сотрудников.'''
print("\nУрок 5 задание 3\n")

import os

salary_fund = 0.0
emp_num = 0

work_dir = os.path.join(os.path.dirname(__file__), "user_file3.txt")
with open(work_dir, "r", encoding="utf-8") as user_file:
    while True:
        str = user_file.readline()
        if not str:
            aver_salary = int(salary_fund / emp_num)
            print(f"\nА средняя ЗП по конторе: {aver_salary}")
            exit()
        else:
            str_list = str.split(' ')
            sec_name = str_list[0]
            salary = float(str_list[1])
            salary_fund += salary
            emp_num += 1
            if salary < 20000:
                print(f"Сотрудник {sec_name} получает ЗП {salary} ...")
