from secrets import choice
import easygui as gui
import gui as g

a = 0
b = 0
operation = ''
ch = ["+", "-", "*"]

# action = buttonbox("Choose:", choices = ch)


def vvod():
    global a, b, operation
    box = gui.multenterbox(g.msg, g.title,
                           fields=['Введите первое число','Введите второе число: '], choices = [ch])
    a = box[0]
    b = box[1]
    operation = box[2]
