strok = str(input())
a = strok.split()
b = []
for i in a:
    b.append(i.lower())
print(b)
b.sort()
for i in range(len(a)):
    for j in range(len(a)):
        if a[i].lower() == b[j]:
            b[j] = a[i]
print(b)