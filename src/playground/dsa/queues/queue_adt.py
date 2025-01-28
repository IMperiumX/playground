from abc import ABC, abstractmethod


class QueueADT(ABC):
    """
    Abstract base class for a Queue
    """

    @abstractmethod
    def enqueue(self, item):
        """
        Adds an item to the end of the queue
        """
        pass

    @abstractmethod
    def dequeue(self):
        """
        Removes and returns the item at the front of the queue
        """
        pass

    @abstractmethod
    def peek(self):
        """
        Returns the item at the front of the queue without removing it
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Checks if the queue is empty
        """
        pass

    @abstractmethod
    def size(self):
        """
        Returns the number of items in the queue
        """
        pass
