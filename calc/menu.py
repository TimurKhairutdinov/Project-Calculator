import complexn as c
import ration as r
import log as l
import out as o
import easygui as gui
import gui as g


def menu():

    a = gui.buttonbox(g.msg, g.title,
                      choices=['Комплексные числа', 'Вещественные числа', 'Логи'])
    if a == 'Комплексные числа':
        o.out_result(c.complex_new())
    elif a == 'Вещественные числа':
        o.out_result(r.ration())
    elif a == 'Логи':
        l.view_log()


def stop_prog():
    a = gui.ynbox('Вы хотите продолжить работу с калькулятором?',
                  choices=['Начать заново', 'Выход'])
    if a:
        return True
    else:
        return False
