import menu
import select as s

import log as l
from init_status import status_prog
from end_prog import stop_prog

while status_prog != False:
    menu.menu()
    s.click()
    l.log(f'Ввод пользователем {s.text_from_user}')
    menu.mn_select(s.text_from_user)
    status_prog = stop_prog()

    
