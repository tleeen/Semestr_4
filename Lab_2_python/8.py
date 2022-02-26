a = int(input('Введите колличество эллементов списка\n'))
b = list()
d = list()
c = 0
for i in range(a):
    print('Введите эллемент списка под индексом [' + str(i) + ']')
    b.append(int(input()))
print(b)
for i in range(a):
    for j in range(i):
        if b[i] == b[j]:
            c += 1
    for k in range(i + 1, a):
        if b[i] == b[k]:
            c += 1
    if c == 0:
        print(b[i])
    c = 0