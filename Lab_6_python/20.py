def cached(func):
    a = {}

    def test(*args):
        if args not in a:
            a[args] = func(*args)
        print(a)
        return a[args]

    return test


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(5))
