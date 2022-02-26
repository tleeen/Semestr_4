a = set()
n = int(input())
for i in range(n):
    a.update(input().split())
print(len(a))
