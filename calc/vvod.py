from secrets import choice
import easygui as gui
import gui as g


def vvod():
    global a, b, op
    box = gui.multenterbox(g.msg,
                           g.title,
                           fields=[
                               'Введите первое число',
                               'Арифметическая операция',
                               'Введите второе число: '
                           ])
    a = box[0]
    op = str(box[1])
    b = box[2]
    print(op)
    print(type(op))
    if op != '+' and op != '-' and op != '*' and op != '/' and op != '//':
        gui.textbox(f'Неккоректный ввод Арифметической операции {op}')
        vvod()
    
