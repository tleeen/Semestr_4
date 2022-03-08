def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print(power(8, 0))
print(power(12, 3))
print(power(1, 10))
print(power(45, 1))