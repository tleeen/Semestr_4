strok = str(input())
a = strok.split()
b = []
for i in range(len(a)):
    b.append(abs(int(a[i])))
print(sorted(b))
