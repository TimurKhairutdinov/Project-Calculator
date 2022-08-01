from random import choice
from easygui import *
import users as us
msg = "Hello, world!"  # Сообщение
title = "Hello, world!"  # Шапка
button = "Ок"  # Кнопка
# msgbox(msg, title, button)
# a = gui.buttonbox('Для доступа к log, необходимо иметь права администратора!',choices =['ок'])
# if a == 'ок':
#     fieldValues = gui.multpasswordbox("Логин", "Пароль")
#     login, password_from_user = fieldValues[0], fieldValues[1]

# find_user_status = False
# for i in us.user.keys():
#     if login == i:
#         find_user_status = True


# if find_user_status != False:
#     password = us.user.get(login)
#     if password_from_user == password:
#         a = gui.buttonbox('Для доступа к log, необходимо иметь права администратора!',
#                           choices=['Войти'])
#         with open('log.txt', 'r', encoding='utf-16') as log:
#             r = log.readlines()
#             a = gui.buttonbox(f'{r}')
#     else:
#         a = gui.buttonbox(f'Неправильный пароль {password_from_user}',
#                           choices=['Войти'])
# else:
#     a = gui.buttonbox('Пользователь не найден',
#                       choices=['Войти'])


