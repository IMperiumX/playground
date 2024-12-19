import abc


class StackADT(metaclass=abc.ABCMeta):
    """
    Abstract base class for a Stack data structure.
    """

    @abc.abstractmethod
    def push(self, item):
        """
        Pushes an item onto the top of the stack.
        """
        pass

    @abc.abstractmethod
    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        """
        pass

    @abc.abstractmethod
    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        """
        pass

    @abc.abstractmethod
    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        pass

    @abc.abstractmethod
    def size(self):
        """
        Returns the number of items in the stack.
        """
        pass
