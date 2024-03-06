name = 'Ed'
age = None

a = 42
print(id(a))
b = 'Hello'
print(id(a))
print(name, age, b, 456, 'text', sep=' (=^.^=)', end='#')
print('Any text')

res = input('Print your text:')
print('You write', res)

ADULT = 18
age = int(input('Сколько тебе лет?'))
how_old = ADULT - age
print(how_old, 'Осталось до совершонелетия')