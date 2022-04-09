class Summator:

    def transform(self, n):
        return n

    def sum(self, N):
        sum = 0
        for i in range(1, N + 1):
            sum += self.transform(i)
        return sum


class SquareSummator(Summator):

    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):

    def transform(self, n):
        return n ** 3


a1 = Summator()
a2 = SquareSummator()
a3 = CubeSummator()

print(a1.sum(3))
print(a2.sum(3))
print(a3.sum(3))
