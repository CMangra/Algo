"""
Aufgabe:

Implement a queue using a singly linked list.

@Chaitanya
Der linked queue funktioniert.

"""
from Wiederholung.LinkedStack import Empty


class LinkedQueue:
    class Node:
        __slots__ = '_element', '_previous'

        def __init__(self, element, next):
            self._element = element
            self._previous = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        if self.is_empty():
            self._head = self.Node(e, None)
            self._tail = self._head
            self._size += 1
        else:
            new_node = self.Node(e, None)
            self._tail._previous = new_node
            self._tail = new_node
            self._size += 1

    def first(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def last(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._tail._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._previous
        self._size -= 1
        return answer


if __name__ == "__main__":
    linkedQueue = LinkedQueue()
    linkedQueue.enqueue(1)
    linkedQueue.enqueue(2)
    linkedQueue.enqueue(3)
    linkedQueue.enqueue(4)
    print(linkedQueue.first())
    print(linkedQueue.last())

    print(linkedQueue.dequeue())
    print(linkedQueue.dequeue())
    print(linkedQueue.dequeue())
    print(linkedQueue.dequeue())
    linkedQueue.enqueue(5)
    print(linkedQueue.dequeue())
