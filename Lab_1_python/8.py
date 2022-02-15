i = 1
s = 0
maximal = 1
minimal = 10000
while True:
    i = input('Введите рост претендента в отряд косманавтов\n')
    if i == '!':
        break
    if 150 <= int(i) <= 190:
        s += 1
        if int(i) > maximal:
            maximal = int(i)
        if int(i) < minimal:
            minimal = int(i)
print(s)
print(minimal, maximal)
