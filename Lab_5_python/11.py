def matrix(*args):
    a = []
    if len(args) == 0:
        a = [[0]]
        return a
    if len(args) == 1:
        a = [[0] * args[0]] * args[0]
        for i in range(args[0]):
            a[i] = [0] * args[0]
        return a
    if len(args) == 2:
        for i in range(args[0]):
            a.append([0] * args[1])
        return a
    if len(args) == 3:
        for i in range(args[0]):
            a.append([args[2]] * args[1])
        return a


rows = matrix()
for row in rows:
    print(*row)

rows = matrix(3)
for row in rows:
    print(*row)

rows = matrix(2, 3)
for row in rows:
    print(*row)

rows = matrix(2, 5, 'a')
for row in rows:
    print(*row)