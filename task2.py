# 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print("Задание 2\n")

totalSec = input("Введите кол-во секунд:\n")
totalSec = int(totalSec)

hours = totalSec // 3600
minutes = (totalSec - hours * 3600) // 60
seconds = totalSec - hours * 3600 - minutes * 60

if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)

print(f"\n{totalSec} секунд - это {hours}:{minutes}:{seconds} (чч:мм:сс)")