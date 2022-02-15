a = int(input('Введите 4-х значное число\n'))
b = a % 10
c = (a // 10) % 10
d = (a // 100) % 10
e = a // 1000
first = 1
second = 1
third = 1
fourth = 1
if b >= c and d >= c and e >= c:
    first = c
    if d >= b and e >= b:
        second = b
        if d >= e:
            third = e
            fourth = d
        else:
            third = d
            fourth = e
    elif b >= d and e >= d:
        second = d
        if b >= e:
            third = e
            fourth = b
        else:
            third = b
            fourth = e
    elif b >= e and d >= e:
        second = e
        if d >= b:
            third = b
            fourth = d
        else:
            third = d
            fourth = b
elif c >= b and d >= b and e >= b:
    first = b
    if d >= c and e >= c:
        second = c
        if d >= e:
            third = e
            fourth = d
        else:
            third = d
            fourth = e
    elif c >= d and e >= d:
        second = d
        if c >= e:
            third = e
            fourth = c
        else:
            third = c
            fourth = e
    elif c >= e and d >= e:
        second = e
        if d >= c:
            third = c
            fourth = d
        else:
            third = d
            fourth = c
elif c >= d and b >= d and e >= d:
    first = d
    if c >= b and e >= b:
        second = b
        if c >= e:
            third = e
            fourth = c
        else:
            third = c
            fourth = e
    elif b >= c and e >= c:
        second = c
        if b >= e:
            third = e
            fourth = b
        else:
            third = b
            fourth = e
    elif b >= e and c >= e:
        second = e
        if b >= c:
            third = c
            fourth = b
        else:
            third = b
            fourth = c
elif c >= e and b >= e and d >= e:
    first = e
    if d >= b and c >= b:
        second = b
        if d >= c:
            third = c
            fourth = d
        else:
            third = d
            fourth = c
    elif b >= d and c >= d:
        second = d
        if b >= c:
            third = c
            fourth = b
        else:
            third = b
            fourth = c
    elif b >= c and d >= c:
        second = c
        if d >= b:
            third = b
            fourth = d
        else:
            third = d
            fourth = b

if first != 0:
    result = first * 1000 + second * 100 + third * 10 + fourth
    print(result)
elif second != 0:
    result = second * 1000 + first * 100 + third * 10 + fourth
    print(result)
elif third != 0:
    result = third * 1000 + first * 100 + second * 10 + fourth
    print(result)
elif fourth != 0:
    result = fourth * 1000 + first * 100 + second * 10 + third
    print(result)
else:
    print('Были введены одни нули')
