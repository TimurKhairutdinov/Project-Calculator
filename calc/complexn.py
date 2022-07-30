import log as l


def complex_num(a, b, operation):
    a = complex(input('Введите комплексное число, например(1+1j): '))
    l.log(a)
    operation = input('Введите операцию: ')
    l.log(operation)
    b = complex(input('Введите комплексное число, например(1+1j): '))
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
