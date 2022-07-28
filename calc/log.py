
import datetime
now = datetime.datetime.now()
def log(text):
    with open('log.txt','a') as log:
        log.writelines(f'\n{now} : {text}')