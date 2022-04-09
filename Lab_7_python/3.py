class Selector:

    def __init__(self, values):
        self.values = values

    def get_odds(self):
        a = []
        for i in self.values:
            if i % 2 == 0:
                a.append(i)
        return a

    def get_evens(self):
        b = []
        for i in self.values:
            if i % 2 == 1:
                b.append(i)
        return b


values = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
