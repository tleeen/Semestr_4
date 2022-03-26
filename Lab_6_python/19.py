def check_password(password):
    def gen(func):
        def test(*args, **kwargs):
            if input('Введите пароль:\n') != password:
                print('Error')
                return None
            return func(*args, **kwargs)

        return test

    return gen


@check_password('123')
def make_burger(TypeOfMeat, withOnion, withTomato):
    if (TypeOfMeat == 'Black Angus') and (withOnion == False) and (withTomato == True):
        print('Like')
    else:
        print('Dislike')


make_burger(TypeOfMeat='Black Angus', withOnion=False, withTomato=True)
