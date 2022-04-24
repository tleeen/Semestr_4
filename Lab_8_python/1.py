import numpy as np

arr_1 = np.full((3, 4), 3)

arr_2 = np.random.randint(0, 10, size=(2, 4))

print(arr_1.size)
print(arr_2.size)

print(np.row_stack((arr_1, arr_2)))

arr_3 = np.array((1, 8, 6, 5, 8, 3))

arr_4 = arr_3 * 3 + 1

arr_5 = arr_3.reshape((2, 3))

print(np.amin(arr_5, 1))

print(arr_5.mean())

arr_6 = np.arange(11) ** 2

print(arr_6[1::2])

print(arr_6[::-1])

arr_6[1::2] = 2

print(49 in arr_6)

A = np.random.randint(-10, 11, size=(4, 4))
B = A[A < 0]
