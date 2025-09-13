from playground.dsa import Stack

from .queue_adt import QueueADT


class QueueOverflowError(Exception):
    """Exception raised when a queue overflow occurs."""

    pass


class QueueUnderflowError(Exception):
    """Exception raised when a queue underflow occurs."""

    pass


class Queue(QueueADT):
    """
    A queue data structure implementation.

    Attributes:
        limit (int): The maximum number of elements the queue can hold.

    Raises:
        QueueOverflowError: If an attempt is made to enqueue an element onto a full queue.
        QueueUnderflowError: If an attempt is made to dequeue or peek an empty queue.
    """

    def __init__(self, limit=10):
        """
        Initializes the queue with an optional limit.

        Args:
            limit (int, optional): The maximum capacity of the queue. Defaults to 10.
        """
        self._queue = Stack(limit=limit)  # Use a protected attribute for internal data
        self.limit = limit

    def __bool__(self):
        """
        Checks if the queue is non-empty.

        Returns:
            bool: True if the queue is non-empty, False otherwise.
        """
        return bool(self._queue)

    def enqueue(self, data):
        """
        Adds an element to the end of the queue.

        Args:
            data: The element to be added to the queue.

        Raises:
            QueueOverflowError: If the queue is full.
        """
        if self.is_full():
            raise QueueOverflowError("Cannot enqueue onto a full queue")
        self._queue.push(data)

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            QueueUnderflowError: If the queue is empty.
        """
        if self.is_empty():
            raise QueueUnderflowError("Cannot dequeue from an empty queue")
        temp_stack = Stack()
        while self._queue:
            temp_stack.push(self._queue.pop())
        data = temp_stack.pop()
        while temp_stack:
            self._queue.push(temp_stack.pop())
        return data

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        Returns:
            The element at the front of the queue.

        Raises:
            QueueUnderflowError: If the queue is empty.
        """
        if self.is_empty():
            raise QueueUnderflowError("Cannot peek into an empty queue")
        temp_stack = Stack()
        while self._queue:
            temp_stack.push(self._queue.pop())
        data = temp_stack.peek()
        while temp_stack:
            self._queue.push(temp_stack.pop())
        return data

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self._queue

    def is_full(self):
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self._queue.size() == self.limit
