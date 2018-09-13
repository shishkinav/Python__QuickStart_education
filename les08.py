# coding: utf-8

# Python. Быстрый старт.
# Занятие 7.

# Домашнее задание: 
#     рисование барабана пистолета сделать функцией, которая принимает координаты базовой точки для рисования барабана;
#     анимацию вращения барабана также сделать функцией.


import turtle
#import tkSimpleDialog   # 2.x Python
import random
import math


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

def draw_picture(startElement, endElement, color):
    for i in range(startElement, endElement):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
        draw_circle(22, color)
        draw_circle(22, "white")
    gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
    if color == "brown": draw_circle(22, "brown")

    return i % 7
    
turtle.speed(0)

gotoxy(0, 0)
turtle.circle(80)
gotoxy(0, 160)
draw_circle(5, "red")

phi = 360 / 7
r = 50

#отрисовка барабана
draw_picture(0, 7, "white")

answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput("Играть?", "Y/N")
    #tkSimpleDialog.askstring("Нарисовать окружность", "Y/N")       # for 2.x Python
    
    if answer == 'Y':
        start = draw_picture(start, random.randrange(7, 100), "brown") #отрисовка анимации

        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))

    else:
        pass