def palindrome(s):
    c = list(s)
    k = ''
    r = ''
    if len(c) % 2 == 0:
        d = len(c) // 2
        for i in range(len(c) - 1, d - 1, -1):
            k += c[i]
        for i in range(d):
            r += c[i]
        if k == r:
            print('Палиндром')
        else:
            print('Не палиндром')
    if len(c) % 2 == 1:
        d = len(c) // 2
        for i in range(len(c) - 1, d, -1):
            k += c[i]
        for i in range(d):
            r += c[i]
        if k == r:
            print('Палиндром')
        else:
            print('Не палиндром')


palindrome(str(input()))