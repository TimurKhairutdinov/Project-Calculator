from fractions import Fraction
import log as l
def r():
    print('Вычисление рациональных чисел.')

    a = Fraction(input('Введите вещественное число 1: '))
    l.log(a)
    operation = input('Введите операцию: ')
    b = Fraction(input('Введите вещественное число 2: '))
    l.log(b)
    answer = 0
    if operation == '+':
        answer = a+b
    elif operation == '-':
        answer = a-b
    elif operation == '*':
        answer = a*b
    elif operation == '/':
        answer = a/b
    return answer


