import easygui as gui
import menu

def stop_prog():
    a=gui.ynbox('Вы хотите продолжить работу с калькулятором?',
              choices=['Начать заново', 'Выход'])
    if a=='Начать заново':
        return True
    else:
        return False
    # else:

    # print(('Вы хотите продолжить работу с калькулятором?\n'
    #        'Для продолжения нажмите enter\n'
    #        'Для выхода введите "n"\n'))
    # n = input('>> ')
    # if n == 'n':
    #     return False
