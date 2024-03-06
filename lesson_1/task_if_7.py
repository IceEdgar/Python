year = int(input('Введите год по формуле yyyyy:'))
if year % 4 != 0:
    print('Обычный')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Високосный')
    else:
        print('Обычный')
else:
    print('Високосный')