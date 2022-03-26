def factorials(n):
    a = 1
    for item in n:
        a = a * (item + 1)
        yield a


items = int(input())
for i in factorials(range(items)):
    print(i)
