login = input('Введите логин\n') not in '@'
address = input('Введите резервный адрес\n') not in '@'
if login is True or address is True:
    print('Логин и резервный адрес были введены верно')
else:
    print('Логин или резервный адрес были введены неверно')
