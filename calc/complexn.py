import log as l
import vvod as v

def complex_new():
    v.vvod()
    print('Вычисление комплексных чисел.')
    a = complex(v.a)
    operation = v.operation
    b = complex(v.b)
    answer = 0
    def complex_num(a, b, operation):
        global answer
        if operation == '+':
            answer = a + b
        elif operation == '-':
            answer = a - b
        elif operation == '*':
            answer = a * b
        elif operation == '/':
            answer = a / b
        return answer
    l.log(f'первое число - {a}, второе - {b}, операция - {operation}, результат - {answer} ')
    return complex_num(a, b, operation)
