class EmptyListError(Exception):
    pass


class OutOfBoundsError(Exception):
    pass


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_node

    def __len__(self):
        return sum(1 for _ in self)

    def __repr__(self):
        return " => ".join(map(str, self))

    def size(self):
        return len(self)

    def empty(self):
        return self.head is None

    def value_at(self, index):
        assert 0 <= index < self.size(), OutOfBoundsError(
            f"Index {index} is out of bounds"
        )

        current = self.head
        for _ in range(index):
            current = current.next_node

        return current.data

    def push_front(self, data):
        new_node = Node(data, next_node=self.head)
        self.head = new_node

    def pop_front(self):
        assert self.head, EmptyListError("List is empty")

        data = self.head.data
        self.head = self.head.next_node
        return data

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def pop_back(self):
        assert self.head, EmptyListError("List is empty")

        if not self.head.next_node:
            data = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next_node:
                prev = current
                current = current.next_node
            data = current.data
            prev.next_node = None
        return data

    def front(self):
        if not self.head:
            return None
        return self.head.data

    def back(self):
        if not self.head:
            return None
        current = self.head
        while current.next_node:
            current = current.next_node
        return current.data

    def insert(self, index, data):
        # - [x] insert(index, value) - insert value at index, so
        #  the current item at that index is pointed to by the new item at the index
        assert 0 <= index < self.size(), OutOfBoundsError(
            f"Index {index} is out of bounds"
        )

        if not self.head and index == 0:
            self.head = Node(data)

        current = self.head

        for _ in range(index):
            prev = current
            current = current.next_node

        new_node = Node(data, next_node=current)
        prev.next_node = new_node

    def erase(self, index):
        # - [x] erase(index) - removes node at given index
        assert 0 <= index < self.size(), OutOfBoundsError(
            f"Index {index} is out of bounds"
        )

        prev = current = self.head
        for _ in range(index):
            prev = current
            current = current.next_node
        prev.next_node = current.next_node

    def value_n_from_end(self, n):
        # - [x] value_n_from_end(n) - returns the value of
        # the node at the nth position from the end of the list
        assert isinstance(n, int), ValueError("n must be integer value")

        if n == 0:
            n = self.size()

        slow = fast = self.head

        for _ in range(abs(n) - 1):
            fast = fast.next_node

        while slow.next_node and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node
        return slow.data

    def reverse(self):
        # - [x] reverse() - reverses the list
        prev = None
        current = self.head

        while current:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev

    def remove_value(self, value):
        # - [x] remove_value(value) - removes the first item
        # in the list with this value
        for idx, node in enumerate(self):
            if node == value:
                index = idx
                break
        self.erase(index)


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
