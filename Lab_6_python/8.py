russian_a = (chr(i + ord('а')) for i in range(32))
for i in range(32):
    if i == 6:
        print(chr(33 + ord('а')))
    print(next(russian_a))