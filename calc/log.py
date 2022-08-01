import datetime
from gettext import find
import users as us
import easygui as gui


def logger(text):

    now = datetime.datetime.now()
    with open('log.txt', 'a', encoding='utf-16') as log:
        log.writelines(f'\n{now} : {text}')


def view_log():
    a = gui.buttonbox('Для доступа к log, необходимо иметь права администратора!',
                      choices=['Войти'])
    if a == 'Войти':
        box = gui.multenterbox('Введите логи и пароль',
                               fields=['Логин: ', 'Пароль: '])
        login, password_from_user = box[0], box[1]
    logger(f'Ввод пользователем login: {login}')
    find_user_status = False
    for i in us.user.keys():
        if login == i:
            find_user_status = True
            logger(f'Пользователь: {login} найден.')

    if find_user_status != False:
        logger(f'Ввод пользователем password: {password_from_user}')
        password = us.user.get(login)
        if password_from_user == password:
            log_in(login, password_from_user)
        else:
            logger(
                f'Пользователь {login} не получил доступ к log, неверный password:{password_from_user}')
            a = gui.buttonbox(f'Неправильный пароль {password_from_user}',
                              choices=['ок'])
    else:
        a = gui.buttonbox('Пользователь не найден',
                          choices=['ок'])
        logger(f'Пользователь: {login} не найден.')


def log_in(login, password_from_user):
        logger(f'login: {login} password: {password_from_user} Complete!')
        with open('log.txt', 'r', encoding='utf-16') as log:
                r = log.readlines()
                a = gui.buttonbox(f'{r}',choices=['ок'])
        logger(f'Пользователь {login} получил доступ к log')
