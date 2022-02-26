a = int(input('Введите колличество эллементов списка\n'))
b = list()
for i in range(a):
    print('Введите эллемент списка под индексом [' + str(i) + ']')
    b.append(int(input()))
print(b)
if a % 2 == 0:
    for i in range(0, a - 1, 2):
        b[i], b[i + 1] = b[i + 1], b[i]
    print(b)
if a % 2 != 0:
    for i in range(0, a - 2, 2):
        b[i], b[i + 1] = b[i + 1], b[i]
    print(b)