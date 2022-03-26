def russian_a(n):
    for item in range(n):
        if item == 6:
            yield chr(33 + ord('а'))
        yield chr(item + ord('а'))


for i in russian_a(32):
    print(i)
