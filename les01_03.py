# coding: utf-8

# Python. Быстрый старт.
# Занятие 3.

# Домашнее задание: 
#                  функциями dir и help исследовать модули os, sys, psutil
#                  вывести максимум информации о системе (ветка №2):
#                    имя текущей директории, платформа (ОС), кодировка файловой системы,
#                    логин пользователя, количество CPU


# Подключение модуля производится командой import.
# Модуль os идет в комплекте с Python'ом.
# psutil - сторонний модуль, нужно установить через pip install psutil
import os
import psutil
import sys


print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давайте поработаем? (Y/N)")
     
if answer == 'Y':
    print("Отлично, хозяин!")
    print("Я умею:")
    print(" [1] - выведу список файлов")
    print(" [2] - выведу информацию о системе")
    print(" [3] - выведу список процессов")
    do = int(input("Укажите номер действия: "))
    
    if do == 1:
        print(os.listdir())
    elif do == 2:
        print('Имя текущей директории: ', os.getcwd())
        print('Платформа ОС: ', sys.platform)
        print('Кодировка файловой системы: ', sys.getfilesystemencoding())
        print('Логин пользователя: ', psutil.users())
        print('Количество CPU: ', psutil.cpu_count(), '\n При этом процессор используется на ', psutil.cpu_percent(), '% ')


    elif do == 3:
        print(psutil.pids())
    else:
        pass
   
# Функция type выводит информацию о типе переменной (объекта)
# Функция dir показывает внутреннее содержимое переменной (объекта) - атрибуты, методы
# Функция help выводит встронную справку об объекте
    
elif answer == 'N':    
    print("До свидания!")
else:
    print("Неизвестный ответ")    