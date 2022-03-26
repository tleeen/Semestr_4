import sys
a = []
for i in sys.stdin:
    b = i.split()
    d = []
    for k in b:
        d.append(int(k))
    a.append(d)
c = sum(a[0])
if all([sum(i) == c for i in a]) and all([sum(j) == c for j in list(zip(*a))]):
    print('YES')
else:
    print('NO')