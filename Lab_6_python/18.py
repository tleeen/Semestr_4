def check_password(func):
    def test(*args, **kwargs):
        if input('Введите пароль:\n') != '123':
            print('Error')
            return None
        return func(*args, **kwargs)

    return test


@check_password
def fibonachi():
    n = int(input('Введиде количество чисел в последовательности\n'))
    fib1 = fib2 = 1
    if n <= 0:
        print('Error')
    elif n == 1:
        print(fib1)
    else:
        print(fib1, fib2, end=' ')
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
            print(fib2, end=' ')


fibonachi()
