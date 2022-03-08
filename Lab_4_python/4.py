a = {'write': 'W', 'read': 'R', 'execute': 'X'}
b = {}

for i in range(int(input())):
    k, *v = input().split()
    b[k] = set(v)

for i in range(int(input())):
    k, v = input().split()
    if a[k] in b[v]:
        print('OK')
    else:
        print('Access denied')