def same_by(characteristic, objects):
    result = []
    for i in objects:
        result.append(characteristic(i))
    for i in result:
        for j in result:
            if i != j:
                return False
    return True


values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')