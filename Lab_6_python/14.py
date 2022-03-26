import math
a1 = []
a2 = []
d = 0
c = dict()
n = int(input('Введите колличество точек\n'))
for i in range(n):
    b = [int(input('Введите координату x' + str(i + 1) + ' точки\n')),
         int(input('Введите координату y' + str(i + 1) + ' точки\n'))]
    a1.append(b)
for j in a1:
    d = math.sqrt(j[0]**2 + j[1]**2)
    c[str(j)] = d
    a2.append(d)
a2 = sorted(a2)
sorted_keys = sorted(c, key=c.get)
for i in range(len(sorted_keys)):
    sorted_keys[i] = sorted_keys[i].split()
for i in range(len(sorted_keys)):
    for j in range(len(sorted_keys[i])):
        result_str = ""
        for k in range(len(sorted_keys[i][j])):
            if (sorted_keys[i][j][k] == "[") or (sorted_keys[i][j][k] == ',') or (sorted_keys[i][j][k] == "]"):
                res_str = sorted_keys[i][j].replace('[', '')
                res_str = res_str.replace(']', '')
                res_str = res_str.replace(',', '')
        sorted_keys[i][j] = int(res_str)
if len(sorted_keys) > 1:
    for i in range(len(a2) - 1):
        for j in range(i + 1, len(a2)):
            if a2[i] == a2[j]:
                if sorted_keys[i][0] > sorted_keys[j][0]:
                    sorted_keys[j][0], sorted_keys[i][0] = sorted_keys[i][0], sorted_keys[j][0]
                    sorted_keys[j][1], sorted_keys[i][1] = sorted_keys[i][1], sorted_keys[j][1]
                elif (sorted_keys[i][0] == sorted_keys[j][0]) and (sorted_keys[i][1] > sorted_keys[j][1]):
                    sorted_keys[j][1], sorted_keys[i][1] = sorted_keys[i][1], sorted_keys[j][1]
                    sorted_keys[j][0], sorted_keys[i][0] = sorted_keys[i][0], sorted_keys[j][0]
print(sorted_keys)
