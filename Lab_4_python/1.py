a = {}

for i in input().split():
    if i in a:
        a[i] = a.get(i) + 1
        print(a.get(i))
    else:
        a[i] = 0
        print(a.get(i))