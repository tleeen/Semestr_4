a = int(input('Введите колличество эллементов списка\n'))
b = list()
for i in range(a):
    print('Введите эллемент списка под индексом [' + str(i) + ']')
    b.append(int(input()))
print(b)
for i in range(a - 1):
    if b[i] < b[i + 1]:
        print(b[i + 1])