a = [2, 3, 43, 3, 5, 865, 32, 565, 1, 5645, 6, 4, 0]
b = [a[i] for i in range(len(a)) if a[i] < 5]
print(b)
