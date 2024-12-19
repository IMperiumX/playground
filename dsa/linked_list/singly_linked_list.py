class EmptyListError(Exception):
    """Custom exception raised when attempting an operation on an empty list."""

    pass


class OutOfBoundsError(Exception):
    """Custom exception raised when an index is out of the valid range."""

    pass


class Node:
    """Represents a node in the linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Implements a singly linked list with optimized operations."""

    def __init__(self, head=None):
        self.head = head
        self._length = 0  # Cache the length for efficiency
        if head:
            self._length = 1
            current = head
            while current.next_node:
                self._length += 1
                current = current.next_node

    def __iter__(self):
        """Allows iteration over the linked list, yielding the data of each node."""
        current = self.head
        while current:
            yield current.data
            current = current.next_node

    def __len__(self):
        """Returns the number of nodes in the linked list (cached)."""
        return self._length

    def __repr__(self):
        """Returns a string representation of the linked list."""
        return " => ".join(map(str, self))

    def size(self):
        """Returns the number of nodes in the linked list (cached)."""
        return self._length

    def empty(self):
        """Checks if the linked list is empty."""
        return self.head is None

    def value_at(self, index):
        """Returns the data at the specified index."""
        if not 0 <= index < self._length:
            raise OutOfBoundsError(f"Index {index} is out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next_node

        return current.data

    def push_front(self, data):
        """Inserts a new node at the beginning of the linked list."""
        self.head = Node(data, next_node=self.head)
        self._length += 1

    def pop_front(self):
        """Removes and returns the data at the front of the list."""
        if not self.head:
            raise EmptyListError("List is empty")

        data = self.head.data
        self.head = self.head.next_node
        self._length -= 1
        return data

    def push_back(self, data):
        """Inserts a new node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self._length += 1

    def pop_back(self):
        """Removes and returns the data at the end of the list."""
        if not self.head:
            raise EmptyListError("List is empty")

        if not self.head.next_node:
            data = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next_node.next_node:  # Stop one before the last node
                current = current.next_node
            data = current.next_node.data
            current.next_node = None
        self._length -= 1
        return data

    def front(self):
        """Returns the data at the front of the list (None if empty)."""
        return self.head.data if self.head else None

    def back(self):
        """Returns the data at the end of the list (None if empty)."""
        if not self.head:
            return None
        current = self.head
        while current.next_node:
            current = current.next_node
        return current.data

    def insert(self, index, data):
        """Inserts a new node with the given data at the specified index."""
        if not 0 <= index <= self._length:
            raise OutOfBoundsError(f"Index {index} is out of bounds")

        if index == 0:
            self.push_front(data)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next_node

        current.next_node = Node(data, next_node=current.next_node)
        self._length += 1

    def erase(self, index):
        """Removes the node at the specified index."""
        if not 0 <= index < self._length:
            raise OutOfBoundsError(f"Index {index} is out of bounds")

        if index == 0:
            self.pop_front()
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next_node

        current.next_node = current.next_node.next_node
        self._length -= 1

    def value_n_from_end(self, n):
        """Returns the value of the node at the nth position from the end."""
        if not isinstance(n, int) or n < 1:
            raise ValueError("n must be a positive integer")

        if n > self._length:
            raise OutOfBoundsError(f"{n} is greater than the list length")

        slow = fast = self.head
        for _ in range(n):
            fast = fast.next_node

        while fast:
            slow = slow.next_node
            fast = fast.next_node

        return slow.data

    def reverse(self):
        """Reverses the linked list in-place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev

    def remove_value(self, value):
        """Removes the first occurrence of a node with the given value."""
        if not self.head:
            return

        if self.head.data == value:
            self.pop_front()
            return

        current = self.head
        while current.next_node:
            if current.next_node.data == value:
                current.next_node = current.next_node.next_node
                self._length -= 1
                return
            current = current.next_node


if __name__ == "__main__":
    ll = LinkedList(
        head=Node(3, next_node=Node(54, next_node=Node(43, next_node=Node(1992))))
    )
    print("----------")
    print(ll)
    print("----------")
    print(f"Size: {ll.size()}")
    print(f"is empty: {ll.empty()}")
    print(f"Value at 2: {ll.value_at(2)}")
    print("pushing front 2002")
    ll.push_front(2002)
    print("----------")
    print(ll)
    print("----------")
    print(f"pop front value: {ll.pop_front()}")
    print("----------")
    print(ll)
    print("----------")
    print(f"pop front value: {ll.pop_front()}")
    print("----------")
    print(ll)
    print("----------")
    print("push back 93: ")
    ll.push_back(93)
    print("----------")
    print(ll)
    print("----------")
    print(f"pop back value: {ll.pop_back()}")
    print("----------")
    print(ll)
    print("----------")
    print(f"pop back value: {ll.pop_back()}")
    print("----------")
    print(ll)
    print("----------")
    print(f"pop back value: {ll.pop_back()}")
    print("----------")
    print(ll)
    print("----------")
    print(f"pop back value: {ll.pop_back()}")
    print("----------")
    print(ll)
    print("----------")
    print(f"is empty: {ll.empty()}")
    print(f"front of list: {ll.front()}")
    print(f"back of list: {ll.back()}")
    print("push back items: ")
    ll.push_back(2002)
    ll.push_back(214)
    ll.push_back(5643)
    ll.push_back(65)
    ll.push_back(13)
    print("----------")
    print(ll)
    print("----------")
    print(f"front of list: {ll.front()}")
    print(f"back of list: {ll.back()}")
    print("----------")
    print(ll)
    print("----------")
    print("insert at idx 4 value: 293 ")
    ll.insert(4, 293)
    print("----------")
    print(ll)
    print("----------")
    print("erase value at 2nd index")
    ll.erase(2)
    print("----------")
    print(ll)
    print("----------")
    print("3rd last node")
    print(ll.value_n_from_end(3))
    print("2nd last node")
    print(ll.value_n_from_end(2))
    print("----------")
    print(ll)
    print("----------")
    print("Reverse the list")
    ll.reverse()
    print("----------")
    print(ll)
    print("----------")
    print("remove value: 293")
    print("remove value: 65")
    ll.remove_value(293)
    ll.remove_value(65)
    print("----------")
    print(ll)
    print("----------")
