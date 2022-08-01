import easygui
from easygui import *
msg = "Hello, world!" #Сообщение
title = "Hello, world!" #Шапка
button = "Ок" #Кнопка
# msgbox(msg, title, button)

def vvod():
    global var1 #Переменная куда будем записывать данные.
    msg = "Введите цифру"
    title = "Ввод переменной" #Шапочка.
    msgbox(msg, title)
vvod()