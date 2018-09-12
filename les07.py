# coding: utf-8

# Python. Быстрый старт.
# Занятие 6.

# Домашнее задание: свободная форма - потренироваться в рисовании с использованием turtle


import turtle
#import tkSimpleDialog   # для 2.x Python
import random
import math


''' Строка в тройных кавычках - многострочная строка.
    Может использоваться в качестве многострочного комментария.
'''

def gotoxy(x, y):
    ''' Функция перевода курсора без рисования линии
    '''
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    
def draw_circle(r, color):
    ''' Функция рисования круга заданного радиуса и цвета
    '''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def draw_rectangle(x1, y1, x2, y2, color):
    ''' Функция рисования прямоугольника по координатам двух диагональных точек
    '''
    turtle.reset()
    gotoxy(x1, y1)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(x2 - x1)
    turtle.left(90)
    turtle.forward(y2 - y1)
    turtle.left(90)
    turtle.forward(x2 - x1)
    turtle.left(90)
    turtle.forward(y2 - y1)
    turtle.end_fill()


def maxElement (a, b):
    list = []
    if min > max:
        list[0] = b
        list[1] = a
    else:
        list[0] = a
        list[1] = b
    return list

    
# Скорость, равная нулю - максимальная    
turtle.speed(0)

gotoxy(0,0)
turtle.circle(80)
gotoxy(0,160)
draw_circle(5, "red")

phi = 360 / 7
r = 50 

for i in range(0,7):
    phi_rad = phi * i * math.pi / 180.0
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
    turtle.circle(22)

    
gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)    
draw_circle(22, "brown")


answer = ''
while answer != 'N':
    answer = turtle.textinput("Нарисовать прямоугольник", "Y/N")
    #tkSimpleDialog.askstring("Нарисовать окружность", "Y/N")       # Для 2.x Python
    
    if answer == 'Y':
        x1 = random.randrange(-200, 200)
        x2 = random.randrange(-200, 200)
        y1 = random.randrange(-200, 200)
        y2 = random.randrange(-200, 200)
        #xArray = maxElement(x1, x2)
        #yArray = maxElement(y1, y2)
        draw_rectangle(x1, y1, x2, y2, 'black')


    else:
        pass