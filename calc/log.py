
import datetime
now = datetime.datetime.now()


def log(text):
    with open('log.txt', 'a', encoding='utf-8') as log:
        log.writelines(f'\n{now} : {text}')
