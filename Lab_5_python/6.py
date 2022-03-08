a = str(None)


def print_without_duplicates(massage):
    global a
    if a != massage:
        print(massage)
    a = massage


print_without_duplicates(str(input()))
print_without_duplicates(str(input()))
print_without_duplicates(str(input()))
print_without_duplicates(str(input()))