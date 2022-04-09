class Summator:

    def transform(self, n):
        return n

    def sum(self, N):
        sum = 0
        for i in range(1, N + 1):
            sum += self.transform(i)
        return sum


class PowerSummator(Summator):

    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):

    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):

    def __init__(self):
        super().__init__(3)


a1 = Summator()
a2 = SquareSummator()
a3 = CubeSummator()
a4 = PowerSummator(6)

print(a1.sum(3))
print(a2.sum(3))
print(a3.sum(3))
print(a4.sum(3))
