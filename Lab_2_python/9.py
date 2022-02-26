a = []
for i in range(8):
    a.append([0] * 8)
for i in range(8):
    x = int(input('Введите первую координату ферзя\n'))
    y = int(input('Введите вторую координату ферзя\n'))
    a[x - 1][y - 1] = 1
for i in range(8):
    for j in range(8):
        if a[i][j] == 1:
            for k in range(j):
                if a[i][k] == 1:
                    print('YES')
                    exit(0)
            for k in range(j + 1, 8):
                if a[i][k] == 1:
                    print('YES')
                    exit(0)
            for k in range(i):
                if a[k][j] == 1:
                    print('YES')
                    exit(0)
            for k in range(i + 1, 8):
                if a[k][j] == 1:
                    print('YES')
                    exit(0)
            k = i - 1
            t = j - 1
            while (k > 0) and (t > 0):
                if a[k][j] == 1:
                    print('YES')
                    exit(0)
                k -= 1
                t -= 1
            k = i + 1
            t = j + 1
            while (k < 8) and (t < 8):
                if a[k][j] == 1:
                    print('YES')
                    exit(0)
                k += 1
                t += 1
            k = i - 1
            t = j + 1
            while (k > 0) and (t < 8):
                if a[k][j] == 1:
                    print('YES')
                    exit(0)
                k -= 1
                t += 1
            k = i + 1
            t = j - 1
            while (t > 0) and (k < 8):
                if a[k][j] == 1:
                    print('YES')
                    exit(0)
                k += 1
                t -= 1
print('NO')