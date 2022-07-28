import log as l


def c():
    print('Вычисление комплексных чисел.')
    a=int(input('Введите первое чиcло: '))
    l.log(a)
    b=int(input('Введите второе число: '))
    l.log(b)
    res = complex(a,b)
    return res
