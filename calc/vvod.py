try:
    a = ''
    b = ''
    operation = ''
except:
    print('Введите правильные значения')

def vvod():
    global a, b, operation
    a = input('Введите первое число: ')
    operation = input('Введите операцию: ')
    b = input('Введите второе число: ')

print(vvod())