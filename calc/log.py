import datetime


def log(text):

    now = datetime.datetime.now()
    with open('log.txt', 'a', encoding='utf-16') as log:
        log.writelines(f'\n{now} : {text}')
