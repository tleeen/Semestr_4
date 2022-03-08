a = {}
for i in range(int(input())):
    line = input().split()
    for j in line:
        a[j] = a.get(j, 0) + 1
for i in sorted(a.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])