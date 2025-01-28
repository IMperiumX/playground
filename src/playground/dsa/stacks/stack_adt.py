from abc import ABC, abstractmethod


class StackADT(ABC):
    """
    Abstract base class for a Stack data structure.
    """

    @abstractmethod
    def push(self, item):
        """
        Pushes an item onto the top of the stack.
        """
        pass

    @abstractmethod
    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        """
        pass

    @abstractmethod
    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        pass

    @abstractmethod
    def size(self):
        """
        Returns the number of items in the stack.
        """
        pass
