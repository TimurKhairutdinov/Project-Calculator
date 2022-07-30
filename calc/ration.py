from fractions import Fraction
import log as l

def ration():
    print('Вычисление рациональных чисел.')
    a = Fraction(input('Введите вещественное число 1: '))
    operation = input('Введите операцию: ')
    b = Fraction(input('Введите вещественное число 2: '))
    answer = 0
    if operation == '+':
        answer = a+b
    elif operation == '-':
        answer = a-b
    elif operation == '*':
        answer = a*b
    elif operation == '/':
        answer = a/b
    l.log(f'первое число - {a}, второе - {b}, операция - {operation}, результат - {answer} ')
    return answer


