N = int(input('Введит значение N\n'))
a = 1
b = 0
if a > 0:
    while a <= N:
        c = ''
        b += 1
        i = 0
        while i < b:
            c = c + str(a) + " "
            a += 1
            if a > N:
                break
            i += 1
        print(c)
else:
    print('Неверное значение N')
