class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

        if step == 0:
            raise StepValueError('шаг не может быть равен 0')


    def __iter__(self):
        self.pointer = self.start
        return self


    def __next__(self):
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration

        value = self.pointer
        self.pointer += self.step
        return value

try:
    iter1 = Iterator(100, 200, 0)  # Это вызовет исключение
except StepValueError as e:
    print(e)


iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1, -1)


print("Iterator from -5 to 1:")
for i in iter2:
    print(i, end=' ')
print()


print("Iterator from 6 to 15 with step 2:")
for i in iter3:
    print(i, end=' ')
print()


print("Iterator from 5 to 1 with step -1:")
for i in iter4:
    print(i, end=' ')
print()


print("Iterator from 10 to 1 with step -1:")
for i in iter5:
    print(i, end=' ')
print()