n = int(input('Введите высоту n\n'))
g = n
m = int(input('Введите ширину m\n'))
symb = input('Введите символ\n')
if n <= 1 or m <= 1:
    print('Неверно введены данные')
else:
    print(str(symb) * m)
    n -= 1
    while n != 1:
        print(str(symb) + " " * (g - 2) + str(symb))
        n -= 1
    print(str(symb) * m)
