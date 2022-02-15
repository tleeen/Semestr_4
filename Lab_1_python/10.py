while True:
    fac = 1
    first_number = int(input('Введите первое число\n'))
    mark = input('Введите символ операции\n')
    if mark == '+':
        second_number = int(input('Введите второе число\n'))
        print(first_number + second_number)
    if mark == '-':
        second_number = int(input('Введите второе число\n'))
        print(first_number - second_number)
    if mark == '*':
        second_number = int(input('Введите второе число\n'))
        print(first_number * second_number)
    if mark == '/':
        second_number = int(input('Введите второе число\n'))
        print(int(first_number / second_number))
    if mark == '%':
        second_number = int(input('Введите второе число\n'))
        print(first_number % second_number)
    if mark == '!':
        if first_number > 0:
            while first_number > 0:
                fac *= first_number
                first_number -= 1
            print(fac)
    if mark == 'x':
        print(first_number)
        break
