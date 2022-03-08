a = {}


def add_friends(name_of_person, list_of_friends):
    global a
    a[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    global a
    for k, v in a.items():
        if k == name_of_person1:
            for i in v:
                if i == name_of_person2:
                    return True
        if k == name_of_person2:
            for i in v:
                if i == name_of_person1:
                    return True
    return False


def print_friends(name_of_person):
    global a
    for k, v in a.items():
        if k == name_of_person:
            v.sort()
            print(v)
            break
        for i in v:
            if i == name_of_person:
                print(k)


add_friends("Соня", ["Маша", "Саша"])
print(are_friends("Маша", "Соня"))
print_friends("Соня")
print_friends("Саша")
print_friends("Маша")
add_friends("Вадим", ["Дима", "Саша"])
print(are_friends("Вадим", "Дима"))
print(are_friends("Вадим", "Маша"))