class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        s = 0
        for i in range(len(self.coefficients)):
            s = s + self.coefficients[i] * x ** i
        return s

    def __add__(self, a):
        c1 = self.coefficients
        c2 = a.coefficients
        if len(c1) < len(c2):
            c1 += [0] * (len(c2) - len(c1))
        else:
            c2 += [0] * (len(c1) - len(c2))
        return Polynomial([c1[i] + c2[i] for i in range(len(c1))])


poly1 = Polynomial([0, 0, 1])
print(poly1(-2))
print(poly1(-1))
print(poly1(0))
print(poly1(1))
print(poly1(2))
print()

poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()

poly3 = poly1 + poly2
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()