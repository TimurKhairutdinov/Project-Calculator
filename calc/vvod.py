import easygui as gui
import gui as g

a = 0
b = 0
operation = ''


def vvod():
    global a, b, operation
    box = gui.multenterbox(g.msg, g.title,
                           fields=['Введите первое число', 'Введите операцию: ', 'Введите второе число: '])
    a = box[0]
    operation = box[1]
    b = box[2]
