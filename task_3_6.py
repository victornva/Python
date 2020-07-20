''' 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
        Например, print(int_func(‘text’)) -> Text.
        Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
        Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
        Необходимо использовать написанную ранее функцию int_func().
'''
print("\nУрок 3 задание 6\n")

def up_case__func(word_str):
    '''
    Ф-ция выставляет певую букву слова в верхний регистр
    :param word_str: str, слово
    :return: str, слово с Большой буквы
    '''
    return word_str[0].upper() + word_str[1:]

user_words = str(input("Введите слова строкой через пробел\n"))
words_list = user_words.split(' ')                 # переводим строку со словами в список слов

new_str = str()                                    # создаём пустую строку для формирования результата
for word in words_list:                            # для каждого слова из списка
    new_str += up_case__func(word.lower()) + ' '   # вызываем нашу ф-цию и формируем строку из слов уже с большой буквы

print("Строка    до: ", user_words)
print("Строка после: ", new_str)
