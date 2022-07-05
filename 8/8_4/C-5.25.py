"""
Aufgabe:

The syntax data.remove(value) for Python list data removes only the first occurrence of element value from the list.
Give an implementation of a function, with signature remove_all(data, value), that removes all occurrences of value
from the given list, such that the worst-case running time of the function is O(n) on a list with n elements. Not that
it is not efficient enough in general to rely on repeated calls to remove.


@Chaitanya
Kommentar: Seite 248 im Buch, Code aus C-5.16.py. Implementierte Methode: remove_all(data, value)
           Ich brauche Hilfe bei der Implementierung der Methode remove_all. Die Methode an sich funktioniert aber die
           Komplexität ist O(n^2). Die Komplexität muss O(n) sein.

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
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.append(5)
    myList.pop()
    myList.pop()

    print(myList)
    print()

    myList.append(5)
    myList.insert(2, 3)
    myList.append(11)
    print(myList)
    print()

    myList.remove(11)
    myList.append(69)
    myList.append(69)
    myList.append(69)
    myList.append(69)
    myList.append(69)
    myList.append(69)
    myList.remove_all(myList, 69)
    print(myList)
    print()

    myList.__setitem__(0, 2)
    print(myList)
