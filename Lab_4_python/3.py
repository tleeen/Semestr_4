a = {}

for i in range(int(input())):
    k, v = input().split()
    a[k] = a.get(k, 0) + int(v)

for k, v in a.items():
    print(k, v)