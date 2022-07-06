"""
Aufgabe:

What values are returned during the following series of stack operations, if
executed upon an initially empty stack? push(5), push(3), pop(), push(2),
push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
pop(), push(4), pop(), pop().

@Chaitanya
Kommentar: Seite 272 im Buch. Program ausführen, um Lösung zu überprüfen-
Lösungsweg:
        Operation       Return Value        Stack Contents
        push(5)         -                   [5]
        push(3)         -                   [5, 3]
        pop()           3                   [5]
        push(2)         2                   [5, 2]
        push(8)         -                   [5, 2, 8]
        pop()           8                   [5, 2]
        pop()           2                   [5]
        push(9)         -                   [5, 9]
        push(1)         -                   [5, 9, 1]
        pop()           1                   [5, 9]
        push(7)         -                   [5, 9, 7]
        push(6)         -                   [5, 9, 7, 6]
        pop()           6                   [5, 9, 7]
        pop()           7                   [5, 9]
        push(4)         -                   [5, 9, 4]
        pop()           4                   [5, 9]
        pop()           9                   [5]

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

    def remove_all(self, data, value):
        for element in data:
            if element == value:
                data.remove(value)

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
            self._resize(self._capacity // 2)


if __name__ == '__main__':
    myList = MyArray()
    myList.append(5)
    myList.append(3)
    myList.pop()
    myList.append(2)
    myList.append(8)
    myList.pop()
    myList.pop()
    myList.append(9)
    myList.append(1)
    myList.pop()
    myList.append(7)
    myList.append(6)
    myList.pop()
    myList.pop()
    myList.append(4)
    myList.pop()
    myList.pop()
    print(myList)
