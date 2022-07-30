import menu
import select
import out
import log as l

status_prog = True
while status_prog != False:
    menu.menu()
    cl = select.click() 
    res = menu.mn_select(cl)
    l.log(res)
    out.out_result(res)
    l.log(res)
