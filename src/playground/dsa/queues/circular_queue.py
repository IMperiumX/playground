# Circular Queue
from typing import Any

from .queue_adt import QueueADT


class QueueOverflowError(Exception):
    """
    An exception raised when an attempt is made to enqueue onto a full queue.
    """

    pass


class QueueUnderflowError(Exception):
    """
    An exception raised when an attempt is made to dequeue from an empty queue.
    """

    pass


class CircularQueue(QueueADT):
    """
    A circular queue data structure implementation.

    Attributes:
        limit (int): The maximum number of elements the queue can hold.
        front (int): The index of the front element in the queue.
        rear (int): The index of the rear element in the queue.
        size (int): The current number of elements in the queue.

    Raises:
        QueueOverflowError: If an attempt is made to enqueue an element onto a full queue.
        QueueUnderflowError: If an attempt is made to dequeue or peek an empty queue.
    """

    def __init__(self, limit=10):
        """
        Initializes the circular queue with an optional limit.

        Args:
            limit (int, optional): The maximum capacity of the queue. Defaults to 10.
        """
        self._queue = [None] * limit  # Use a protected attribute for internal data
        self.limit = limit
        self.front = 0
        self.rear = 0
        self.size = 0

    def __bool__(self):
        """
        Checks if the circular queue is non-empty.

        Returns:
            bool: True if the circular queue is non-empty, False otherwise.
        """
        return bool(self.size)

    def is_full(self):
        """
        Checks if the circular queue is full.

        Returns:
            bool: True if the circular queue is full, False otherwise.
        """
        return self.size == self.limit

    def is_empty(self):
        """
        Checks if the circular queue is empty.

        Returns:
            bool: True if the circular queue is empty, False otherwise.
        """
        return self.size == 0

    def enqueue(self, data: Any):
        """
        Adds an element to the end of the circular queue.

        Args:
            data: The element to be added to the circular queue.

        Raises:
            QueueOverflowError: If the circular queue is full.
        """
        if self.is_full():
            raise QueueOverflowError("Cannot enqueue onto a full circular queue")
        self._queue[self.rear] = data
        self.rear = (self.rear + 1) % self.limit
        self.size += 1

    def dequeue(self):
        """
        Removes and returns the element at the front of the circular queue.

        Returns:
            Any: The element at the front of the circular queue.

        Raises:
            QueueUnderflowError : If the circular queue is empty.
        """
        if self.is_empty():
            raise QueueUnderflowError("Cannot dequeue from an empty circular queue")
        data = self._queue[self.front]
        self._queue[self.front] = None
        self.front = (self.front + 1) % self.limit
        self.size -= 1
        return data

    def peek(self):
        """
        Returns the element at the front of the circular queue without removing it.

        Returns:
            Any: The element at the front of the circular queue.

        Raises:
            QueueUnderflowError: If the circular queue is empty.
        """
        if self.is_empty():
            raise QueueUnderflowError("Cannot peek into an empty circular queue")
        return self._queue[self.front]

    def size(self):
        """
        Returns the number of elements in the circular queue.

        Returns:
            int: The number of elements in the circular queue.
        """
        return self.size

    def __repr__(self):
        """
        Returns the string representation of the circular queue.

        Returns:
            str: The string representation of the circular queue.
        """
        return f"CircularQueue({self._queue})"

    def __str__(self):
        """
        Returns the string representation of the circular queue.

        Returns:
            str: The string representation of the circular queue.
        """
        return str(self._queue)
