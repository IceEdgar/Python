# Задание №5
# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n, e, = 10, 5
n_sum = 0
elem = 0

while elem <= n:
    elem += 1
    if elem % 2 == 0 and elem % e != 0:
        n_sum += elem
        print(n_sum)
        continue
print(n_sum)
"""
n = 100
e = 3
sum = 0

while (n >= 1):
    if ((n % e) != 0) and ((n % 2) !=0):
            sum += n                 0):
     n -= 1
 sum

"""