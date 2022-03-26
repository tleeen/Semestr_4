from sys import stdin
a = []
for i in stdin.read().replace('.', '').split():
    a.append(i)
b = list(filter(lambda x: x[1].istitle(), enumerate(a)))
b = sorted(b, key=lambda x: x[1])
c = []
d = set()
for i in b:
    if i[1] not in d:
        c.append(i)
        d.add(i[1])
for pair in c:
    print(pair[0], ' - ', pair[1])
