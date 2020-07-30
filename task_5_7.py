'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
    Если фирма получила убытки, в расчет средней прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

    Подсказка: использовать менеджеры контекста.
'''

print("\nУрок 5 задание 7\n")

import os
import json

firms_dic = {}
average_profit = 0

work_dir = os.path.join(os.path.dirname(__file__), "user_file7.txt")
with open(work_dir, "r", encoding="utf-8") as user_file:

    while True:
        firm = user_file.readline()
        if not firm:

            profit_dic = dict({"average_profit": average_profit})
            new_list = [firms_dic, profit_dic]
            print(new_list)

            json_dir = os.path.join(os.path.dirname(__file__), "data.json")
            with open(json_dir, "w") as json_file:
                #json_file.write(json.dumps(new_list, ensure_ascii = False))
                json.dump(new_list, json_file, ensure_ascii=False)

            exit()
        else:
            firm_list = firm.split(' ')
            profit = float(firm_list[2]) - float(firm_list[3])
            firms_dic[firm_list[0]] = profit

            if profit > 0:
                average_profit += profit
