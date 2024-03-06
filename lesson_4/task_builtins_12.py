'''globals()'''


SIZE = 10


def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z


print(globals())
print(func(1, 2, 3))

#Внимание! Если вызвать функцию locals() из основного кода модуля, а не из функции, результат будет аналогичен работе функции globals()

x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(x)