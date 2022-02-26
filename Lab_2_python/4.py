a = str(input('Введите строку\n'))
minimal = 1000000
maximal = -1
b = 0
for i in range(len(a)):
    if a[i] == 'f':
        b = b + 1
if b == 1:
    for i in range(len(a)):
        if a[i] == 'f':
            b = i
    print('Буква f встретилась в строке один раз. Вот её индекс: [' + str(b) + ']')
elif b > 1:
    for i in range(len(a)):
        if a[i] == 'f':
            if i < minimal:
                minimal = i
            elif i > maximal:
                maximal = i
    print('Буква f встретилась несколько раз. Вот индексы: [' + str(minimal) + '] и [' + str(maximal) + ']')
