class SparceArray:

    def __init__(self):
        self.a = {}

    def __getitem__(self, item):
        return self.a.get(item, 0)

    def __setitem__(self, key, value):
        self.a[key] = value


arr = SparceArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))