a = str(input('Введите строку\n'))
minimal = 1000000
maximal = -1
for i in range(len(a)):
    if a[i] == 'h':
        if i < minimal:
            minimal = i
        elif i > maximal:
            maximal = i
print(a[maximal - 1:minimal:-1])