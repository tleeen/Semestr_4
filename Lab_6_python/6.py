def square_fibonacci(n):
    fib1 = 1
    fib2 = 1
    if n == 1:
        yield 1
    elif n == 2:
        yield 1
        yield 1
    else:
        yield 1
        yield 1
        for item in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
            yield fib2**2


items = int(input())
for i in square_fibonacci(items):
    print(i)
