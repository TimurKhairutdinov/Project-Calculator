import easygui as gui


def stop_prog():
    gui.ynbox('Вы хотите продолжить работу с калькулятором?',
              choices=['Начать заново', 'Выход'])
    # print(('Вы хотите продолжить работу с калькулятором?\n'
    #        'Для продолжения нажмите enter\n'
    #        'Для выхода введите "n"\n'))
    # n = input('>> ')
    # if n == 'n':
    #     return False
