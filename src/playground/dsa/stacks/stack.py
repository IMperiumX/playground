class StackOverflowError(Exception):
    """Exception raised when a stack overflow occurs."""

    pass


class StackUnderflowError(Exception):
    """Exception raised when a stack underflow occurs."""

    pass


class Stack:
    """
    A stack data structure implementation.

    Attributes:
        limit (int): The maximum number of elements the stack can hold.

    Raises:
        StackOverflowError: If an attempt is made to push an element onto a full stack.
        StackUnderflowError: If an attempt is made to pop or peek an empty stack.
    """

    def __init__(self, limit=10):
        """
        Initializes the stack with an optional limit.

        Args:
            limit (int, optional): The maximum capacity of the stack. Defaults to 10.
        """
        self._stack = []  # Use a protected attribute for internal data
        self.limit = limit

    def __bool__(self):
        """
        Checks if the stack is non-empty.

        Returns:
            bool: True if the stack is non-empty, False otherwise.
        """
        return bool(self._stack)

    def push(self, data):
        """
        Pushes an element onto the top of the stack.

        Args:
            data: The element to be pushed onto the stack.

        Raises:
            StackOverflowError: If the stack is full.
        """
        if self.is_full():
            raise StackOverflowError("Cannot push onto a full stack")
        self._stack.append(data)

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Returns:
            The element at the top of the stack.

        Raises:
            StackUnderflowError: If the stack is empty.
        """
        if self.is_empty():
            raise StackUnderflowError("Cannot pop from an empty stack")
        return self._stack.pop()

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            The element at the top of the stack.

        Raises:
            StackUnderflowError: If the stack is empty.
        """
        if self.is_empty():
            raise StackUnderflowError("Cannot peek an empty stack")
        return self._stack[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not bool(self._stack)

    def is_full(self):
        """
        Checks if the stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return self.size() >= self.limit

    def size(self):
        """
        Returns the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self._stack)

    def __contains__(self, item):
        """
        Checks if an item is present in the stack.

        Args:
            item: The item to search for.

        Returns:
            bool: True if the item is in the stack, False otherwise.
        """
        return item in self._stack

    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return str(self._stack)

    def __len__(self):
        """
        Returns the size of the stack

        Returns:
            int: The number of elements in the stack.
        """
        return len(self._stack)

    def __repr__(self):
        """
        Returns the representation of a stack class.

        Returns:
             str: A string of class representation.
        """
        return f"Stack(limit={self.limit})"


if __name__ == "__main__":
    try:
        stack = Stack(limit=5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print(f"Stack contents: {stack}")  # Output: Stack contents: [1, 2, 3]
        print(f"Stack size: {len(stack)}")  # Output: Stack size: 3
        print(f"Top element: {stack.peek()}")  # Output: Top element: 3
        print(f"Popped element: {stack.pop()}")  # Output: Popped element: 3
        print(f"Is 2 in the stack? {2 in stack}")  # Output: Is 2 in the stack? True
        print(f"Is stack empty? {stack.is_empty()}")  # Output: Is stack empty? False
        stack.push(4)
        stack.push(5)
        stack.push(6)
        stack.push(7)  # This will raise a StackOverflowError
    except StackOverflowError as e:
        print(f"Error: {e}")  # Output: Error: Cannot push onto a full stack
    except StackUnderflowError as e:
        print(f"Error: {e}")
