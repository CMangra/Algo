import ctypes


class MyArray:
    def __init__(self):
        self._numberOfItems = 0
        self._capacity = 1
        self._Array = self.__make_array(self._capacity)

    def __make_array(self, capacity):
        return(capacity*ctypes.py_object)()

    def __len__(self):
        return self._numberOfItems

    def __getitem__(self, k):
        if not 0 <= k < self._numberOfItems:
            raise IndexError('invalid index')
        return self._Array[k]

    def append(self, obj):
        if self._numberOfItems == self._capacity:
            self._resize(2*self._capacity)
        self._Array[self._numberOfItems] = obj
        self._numberOfItems += 1

    def _resize(self, capacity):
        NewArray = self.__make_array(capacity)
        for k in range(self._numberOfItems):
            NewArray[k] = self._Array[k]
        self._Array=NewArray
        self._capacity = capacity
        
l = MyArray()

print(len(l))

l.append(50)

print(len(l))

l.append(50)

print(len(l))

l.append(50)

print(len(l))
l.append(50)

print(len(l))
l.append(50)

print(len(l))