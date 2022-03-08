a = {}

for i in range(int(input())):
    k, v = input().split()
    a[k] = v

word = str(input())

for k, v in a.items():
    if k == word:
        print(v)
    if v == word:
        print(k)