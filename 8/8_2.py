import ctypes


class MyArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __setitem__(self, k, value):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        self._A[k] = value

    def insert(self, k, value):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        end = self._A[k:]
        self._A[k] = value
        self._n += 1
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in end:
            k += 1
            self._A[k] = j

    def remove(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        end = self._A[k + 1:]
        for j in end:
            self._A[k] = j
            k += 1
        self._A[k] = None
        self._n -= 1

    def _toString_(self):
        for element in self._A:
            print(str(element) + ",")


if __name__ == '__main__':
    data = MyArray()
    data.append(1)
    data.append(2)
    data.append(3)
    data.append(4)
    data.remove(2)
    data.insert(2, 3)
    print(data._toString_())
    #data.remove(3)
    print(data._A)
    data.__setitem__(0, 2)
    print(data._A)
