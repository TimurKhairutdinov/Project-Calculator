import menu
import select
import out
import log as l

menu.menu()

cl =  select.click()
l.log(cl)
res = menu.mn_select(cl)
l.log(res)
out.out_result(res)
l.log(res)