def power(a, n):
    c = 1
    if n < 0:
        for i in range(abs(n)):
            c = c * 1/a
        return c
    elif n == 0:
        return c
    else:
        for i in range(abs(n)):
            c = c * a
        return c


print(power(float(input()), int(input())))