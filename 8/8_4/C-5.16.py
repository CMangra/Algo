"""
Aufgabe:

Implement a pop method for the DynamicArray class, given in Code Fragment 5.3, that removes the last element of the
array, and that shrinks the capacity, N, of the array by half any time the number of elements in the array goes below
N/4.

@Chaitanya
Kommentar:  Code aus 8_3.py. Im Buch Seite 218. Aufgabe: implement pop function.

"""

import ctypes


class MyArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        elif k < 0:
            k = abs(k)
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
        if not 0 <= k < len(self._A):
            raise IndexError('invalid index')

        end = self._A[k:self._n]
        self._A[k] = value
        if len(self._A) + 1 >= self._capacity:
            self._resize(2 * self._capacity)
        counter = 0
        for i in range(k + 1, k + len(end) + 1):
            self._A[i] = end[counter]
            counter += 1
        self._n += 1

    def remove(self, k):
        for i in range(self._n):
            if self._A[i] == k:
                position_deleted = i
                if position_deleted == self._n - 1:
                    end = []
                else:
                    end = self._A[position_deleted + 1:self._n]

                for j in end:
                    self._A[position_deleted] = j
                    position_deleted += 1
                self._n -= 1

    def __str__(self):
        r = ""
        counter = 0
        while counter < self._n:
            r += str(self._A[counter]) + " "
            counter += 1
        return r

    def pop(self):
        self._A = self._A[0:self._n - 1]
        self._n -= 1
        self._resize(self._capacity)
        if self._n < self._capacity // 4:
            self._resize(self._capacity//2)


if __name__ == '__main__':
    data = MyArray()
    data.append(1)
    data.append(2)
    data.append(3)
    data.append(4)
    data.append(5)
    data.pop()
    data.pop()

    print(data)
    print()

    data.append(5)
    data.insert(2, 3)
    print(data)
    print()

    data.remove(3)
    print(data)
    print()

    data.__setitem__(0, 2)
    print(data)
