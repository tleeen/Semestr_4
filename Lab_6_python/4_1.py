a = [2, 3, 43, 3, 5, 865, 32, 565, 1, 5645, 6, 4, 0]
b = list(map(lambda i: i / 2, filter(lambda i: i > 17, a)))
print(b)
