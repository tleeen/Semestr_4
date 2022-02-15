while True:
    password = input('Введеите пароль\n')
    if len(password) > 7:
        if password.find("123") == -1:
            password_2 = input('Подтвердите пароль\n')
            if password == password_2:
                print('OK\n')
                break
            else:
                print('Различаются/n')
        else:
            print('Простой!\n')
    else:
        print('Короткий!\n')
