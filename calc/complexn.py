import log as l


def complex_new():
    print('Вычисление комплексных чисел.')
    a = complex(input('Введите комплексное число, например(1+1j): '))
    operation = input('Введите операцию: ')
    b = complex(input('Введите комплексное число, например(1+1j): '))
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
