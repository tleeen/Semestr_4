class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        super().__init__(a, a, a)


t1 = Triangle(3, 6, 9)
t2 = EquilateralTriangle(2)
print(t1.perimetr())
print(t2.perimetr())
