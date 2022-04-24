import random

with open("6_lines.txt", "r") as file:
    a = file.readlines()
    print(random.choice(a))
