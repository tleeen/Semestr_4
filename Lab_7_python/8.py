class Queue:

    def __init__(self, *values):
        self.values = values

    def append(self, *values):
        self.values = (*self.values, *values)

    def copy(self):
        return Queue(*self.values)

    def pop(self):
        value, self.values = self.values[0], self.values[1:]
        return value

    def extend(self, queue):
        self.values = (*self.values, *queue.values)

    def next(self):
        return Queue(*self.values[1:])

    def __add__(self, other):
        return Queue(*self.values, *other.values)

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.values == other.values

    def __str__(self):
        return f"[{' -> '.join(map(str, self.values))}]" if self.values else "[]"

    def __rshift__(self, n: int):
        return Queue(*self.values[n:]) if n < len(self.values) else Queue()

    def __next__(self):
        return self.next()


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep='\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)