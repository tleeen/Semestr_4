def hello():
    print("Hello")


class A:

    def __str__(self):
        return "A.__str_method"


def good_evening():
    print("Good evening")


class B:

    def __str__(self):
        return "B.__str_method"


class C(A, B):
    pass


class D(B, A):
    pass


c = C()
hello()
good_evening()
d = D()
hello()
good_evening()
print(c)
print(d)
