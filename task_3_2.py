''' 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
   Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой. '''
print("\nУрок 3 задание 2\n")

# принимаем параметры в нескольких отдельных аргументах, составляем из них кортеж и возвращаем его
def user_data_func(f_name, s_name, born, residence, email, phone):
    '''
    Принимает параметры как именованные аргументы, выводит данные о пользователе одной строкой
    :param f_name: str, имя
    :param s_name: str, фамилия
    :param born: int, год рождения
    :param residence: str, город
    :param email: str, эл.почта
    :param phone: str, телефон
    :return: tuple
    '''
    user_data = (f_name, s_name, born, residence, email, phone)
    return user_data

try:
    user_fname = str(input("Введите имя\n"))
    user_sname = str(input("фамилию\n"))
    user_yborn = int(input("год рождения\n"))
    user_res = str(input("проживает в\n"))
    user_email = str(input("эл.почта\n"))
    user_phone = str(input("телефон\n"))
except ValueError:
    print('Неверный формат')
    exit()

# вызываем ф-цию с именованными аргументами, с изменённым их порядком
print('Данные пользователя: ', user_data_func(s_name = user_sname, f_name = user_fname, born = user_yborn, residence = user_res, phone = user_phone, email = user_email))

# то же самое через лямбду
l_user_func = lambda f_name, s_name, born, residence, email, phone: (f_name, s_name, born, residence, email, phone)
print('Данные пользователя: ', l_user_func(phone = user_phone, s_name = user_sname, f_name = user_fname, born = user_yborn, residence = user_res, email = user_email))
