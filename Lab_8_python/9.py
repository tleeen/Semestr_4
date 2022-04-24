with open("9_input.txt", "r") as in_file:
    a = in_file.read().split()

data = [int(i) for i in a]

p = []
m = []
z = []

for i in data:
    if i > 0:
        p.append(i)
    elif i < 0:
        m.append(i)
    else:
        z.append(i)

with open("9_output.txt", "w") as out_file:
    out_file.write(str(len(data)) + "\n1 " + str(len(p)) +
                   " -1 " + str(len(m)) + " 0 " + str(len(z)))
