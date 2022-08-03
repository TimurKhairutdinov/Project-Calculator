from fractions import Fraction
import log as l
import calculation as c
import vvod as v


def ration():
    v.vvod()
    a = Fraction(v.a)
    operation = v.op
    b = Fraction(v.b)
    c.calc(a, b, operation)
    answer = c.answer
    l.logger(f'первое число - {a}, второе - {b}, операция - {operation}, результат - {answer} ')
    return answer
