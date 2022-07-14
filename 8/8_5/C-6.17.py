"""
Aufgabe:
In the previous exercise, we assume that the underlying list is initially
empty. Redo that exercise, this time preallocating an underlying list with
length equal to the stack’s maximum capacity


@Chaitanya
Kommentar:  Funktioniert
"""
from Wiederholung.LinkedStack import Empty


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, max_capacity):
        """Create an empty stack."""
        self._max_capacity = max_capacity
        self._data = [None] * max_capacity  # nonpublic list instance
        self._n = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._n

    def is_empty(self):
        """Return True if the stack is_empty."""
        return self._n == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._n == self._max_capacity:
            raise Empty('Stack is full')
        self._data[self._n] = e  # new item stored at end of list
        self._n += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is_empty.
        """
        if self.is_empty():
            raise Empty('Stack is_empty')
        return self._data[self._n - 1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is_empty.
        """
        if self.is_empty():
            raise Empty('Stack is_empty')

        self._n -= 1
        return self._data.pop()  # remove last item from list


if __name__ == '__main__':
    stack = ArrayStack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    # stack.push(3)        #Exception case
    print(stack.top())
