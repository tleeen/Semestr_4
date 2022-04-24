import numpy as np


def make_field(size):
    a = np.zeros((size, size), dtype=np.int8)
    a[::2, 1::2] = 1
    a[1::2, ::2] = 1
    print(a)


make_field(10)
