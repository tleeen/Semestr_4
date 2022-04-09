class ReversedList:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        return self.list[-1 - item]


r1 = ReversedList([10, 20, 30])
for i in range(len(r1)):
    print(r1[i])
