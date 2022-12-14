from dbl_linked_list import DblLinked_List


class Queue(object):

    """The Queue Data structure is a compoisition of a Double Linked List.

    Methods:
            enqueue(val):  Add a new node to the end (tail) of the queue.

            dequeue():     Remove the node at the head of the queue.

            peek():        Return value at head of queue.

            size():        Return size of queue.

    """

    def __init__(self, maybe_an_iterable=None):
        """Initialize Queue as a DblLinked_List-esque object."""
        try:
            self._container = DblLinked_List(maybe_an_iterable[::-1])
        except TypeError:
            self._container = DblLinked_List(maybe_an_iterable)

    def enqueue(self, value):
        """Add a new node with given value to the end (tail) of the queue."""
        self._container.append(value)

    def dequeue(self):
        """Remove the node at the head of the queue and return the value."""
        try:
            return self._container.pop()
        except IndexError:
            raise IndexError("Cannot dequeue from empty queue.")

    def peek(self):
        """Return the value at the head of the queue.  None if empty."""
        try:
            return self._container.head.value
        except AttributeError:
            return None

    def size(self):
        """Return the size of the queue."""
        return self._container._size

    def __len__(self):
        """Allow use of len() function."""
        return self.size()
