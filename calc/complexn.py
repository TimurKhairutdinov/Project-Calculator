import log as l
import vvod as v
import calculation as c


def complex_new():
    v.vvod()
    a = complex(v.a)
    operation = v.op
    b = complex(v.b)
    c.calc(a, b, operation)
    answer = c.answer
    l.logger(f'первое число - {a}, второе - {b}, операция - {operation}, результат - {answer} ')
    return answer
