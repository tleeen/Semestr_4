import csv

school = input("Введите школу: ")
class_ = input("Введите класс: ")
a = []

with open("rez.csv", "r", encoding="utf-8") as rez_file:
    b = csv.DictReader(rez_file, delimiter=",")
    for i in b:
        login = i["login"]
        i_school = login[12:14]
        i_class = login[15:17]
        if i_school == school and i_class == class_:
            i_name = i["user_name"]
            name = i_name[8:-2]
            score = i["Score"]
            a.append((name, score))

a = sorted(a, key=lambda student: student[0], reverse=True)
a = sorted(a, key=lambda student: -int(student[1]))
for i in a:
    print(*i)
