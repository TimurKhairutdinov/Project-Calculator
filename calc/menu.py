import complexn
import ration
import log as l

def menu():
    print((
        'Вас приветствует калькулятор!\n' 
        'Для работы с рациональными или комплексными числами выберите режим:\n'
        'Введите 1 или 2.\n'
        '1. Рациональные.\n'
        '2. Комплексные.\n'
        '------------------'
    ))

def mn_select(cl):
    status = False
    while status != True:
        if cl == '1':
            res = ration.r()
            status = True
        elif cl == '2':
            res = complexn.c()
            status = True
        else:
            print(('Неккоректный ввод! Введите 1 или 2!\n'
                    '----------------------------------'))
            cl = input()
    return res
