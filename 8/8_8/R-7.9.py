"""
Aufgabe:

Give a fast algorithm for concatenating two doubly linked lists L and M,
with header and trailer sentinel nodes, into a single list L'.

@Chaitanya
Wichtig, um die Aufgabe zu verstehen:
    Header and Trailer Sentinels
    In order to avoid some special cases when operating near the boundaries of a doubly
    linked list, it helps to add special nodes at both ends of the list: a header node at the
    beginning of the list, and a trailer node at the end of the list. These “dummy” nodes
    are known as sentinels (or guards), and they do not store elements of the primary
    sequence.

Kommentar:  concatenate_queue_at_the_end_of_this_queue_and_return_new_queue(self, queue_to_be_concatenated) Methode
            implementiert.

            Die Methode funktioniert.

            Die asserts musste implementiert werden, weil ich den Fall, wo eins von den Queues leer ist, nicht
            berücksichtigt habe.
"""
from Wiederholung.LinkedStack import Empty


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'  # streamline memory

        def __init__(self, element, prev, next):  # initialize node’s fields
            self._element = element  # user’s element
            self._prev = prev  # previous node reference
            self._next = next  # next node reference

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # trailer is after header
        self._trailer._prev = self._header  # header is before trailer
        self._size = 0  # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element  # return deleted element


class LinkedDeque(_DoublyLinkedBase):  # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element  # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element  # real item just before trailer

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.
       
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)  # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.
       
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)  # use inherited method

    def concatenate_queue_at_the_end_of_this_queue_and_return_new_queue(self, queue_to_be_concatenated):
        assert self._size != 0
        assert queue_to_be_concatenated._size != 0
        new_queue = LinkedDeque()
        last_node_of_first_queue = self._trailer._prev
        first_node_of_second_queue = queue_to_be_concatenated._header._next
        last_node_of_first_queue._next = first_node_of_second_queue
        first_node_of_second_queue._prev = last_node_of_first_queue
        new_queue._header = self._header
        new_queue._trailer = queue_to_be_concatenated._trailer
        new_queue._size = len(first_queue) + len(second_queue)
        return new_queue


if __name__ == "__main__":
    first_queue = LinkedDeque()
    second_queue = LinkedDeque()

    first_queue.insert_first(2)
    first_queue.insert_first(1)

    second_queue.insert_first(3)
    second_queue.insert_last(4)
    second_queue.insert_last(69)

    """
    @Chaitanya
    new_queue should now be trailer -> [69, 4, 3, 2, 1] <- header
    """
    new_queue = first_queue.concatenate_queue_at_the_end_of_this_queue_and_return_new_queue(second_queue)

    print(new_queue.delete_first())
    print(new_queue.delete_first())
    print(new_queue.delete_first())
    print(new_queue.delete_first())
    print(new_queue.delete_first())