class Balance:
    le = 0
    ri = 0

    def add_right(self, a):
        self.ri += a

    def add_left(self, a):
        self.le += a

    def result(self):
        if self.ri == self.le:
            return "="
        elif self.ri > self.le:
            return "R"
        else:
            return "L"


balance = Balance()
balance.add_right(100)
balance.add_left(200)
balance.add_left(101)
print(balance.result())
