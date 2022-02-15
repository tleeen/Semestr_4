high = int(input('Введите высоту пирамиды\n'))
d = 1
while high > 0:
    a = " "
    b = "*"
    high = high - 1
    print(a*high+b*d)
    d = d + 2
