def arithmetic_operation(n):
    if n == '+':
        return lambda x, y: x + y
    elif n == '-':
        return lambda x, y: x - y
    elif n == '*':
        return lambda x, y: x * y
    elif n == '/':
        return lambda x, y: x / y
    else:
        return lambda x, y: print('Неверный ввод')


operation = arithmetic_operation('*')
print(operation(12, 4))
