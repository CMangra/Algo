"""
Aufgabe:

Implement a function that counts the number of nodes in a circularly
linked list.

@Chaitanya
Kommentar:  Code im Buch Seite 290
            number_of_nodes() Methode implementiert

"""
from Wiederholung.LinkedStack import Empty


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    class _Node:
        def __init__(self, element, next_element):
            self._element = element
            self._next = next_element

    def __init__(self):
        """Create an empty queue."""
        self._tail = None  # will represent tail of queue
        self._size = 0  # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:  # removing only element
            self._tail = None  # queue becomes empty
        else:
            self._tail._next = oldhead._next  # bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)  # node will be new tail node
        if self.is_empty():
            newest._next = newest  # initialize circularly
        else:
            newest._next = self._tail._next  # new node points to head
            self._tail._next = newest  # old tail points to new node
        self._tail = newest  # new node becomes the tail
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes new tail

    def number_of_nodes(self):
        answer = 0
        if self.is_empty():
            answer = 0
        else:
            is_more_elements = True
            current_node = self._tail._next
            while is_more_elements:
                answer += 1
                current_node = current_node._next
                if current_node == self._tail._next:
                    is_more_elements = False

        return answer


if __name__ == "__main__":
    # Uncomment according to your needs

    circularQueue = CircularQueue()
    circularQueue.enqueue(0)
    circularQueue.enqueue(1)
    circularQueue.enqueue(2)
    circularQueue.enqueue(3)
    # circularQueue.enqueue(4)
    # circularQueue.enqueue(5)
    # circularQueue.enqueue(6)
    # circularQueue.enqueue(7)
    # circularQueue.enqueue(8)
    # circularQueue.enqueue(9)
    # circularQueue.enqueue(10)
    # circularQueue.enqueue(11)
    # circularQueue.enqueue(12)
    # circularQueue.enqueue(13)

    # circularQueue.dequeue() #1
    # circularQueue.dequeue() #2
    # circularQueue.dequeue() #3
    # circularQueue.dequeue() #4
    # circularQueue.dequeue() #5
    # circularQueue.dequeue() #6
    # circularQueue.dequeue() #7
    # circularQueue.dequeue() #8
    # circularQueue.dequeue() #9
    # circularQueue.dequeue() #10
    # circularQueue.dequeue() #11
    # circularQueue.dequeue() #12
    # circularQueue.dequeue() #13
    # circularQueue.dequeue() #14

    print(circularQueue.number_of_nodes())
