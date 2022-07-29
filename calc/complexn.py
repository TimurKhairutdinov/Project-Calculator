a = complex(input('Введите комплексное число, например(1+1j): '))
operation = input('Введите операцию: ')
b = complex(input('Введите комплексное число, например(1+1j): '))


def complex_num(a, b, operation):
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


print(complex_num(a, b, operation))
