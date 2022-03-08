def triangle(a, b, c):
    if a + c > b and b + c > a and b + a > c:
        print('Треугольник')
    else:
        print('Не треугольник')


triangle(int(input()), int(input()), int(input()))
