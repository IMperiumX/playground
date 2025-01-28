from playground.dsa import LinkedList, Node, StackADT


class SinglyListStack(StackADT):
    def __init__(self):
        self._stack = LinkedList(Node(None))

    def __str__(self):
        return str(self._stack)

    def push(self, item):
        self._stack.push_front(item)

    def pop(self):
        return self._stack.pop_front()

    def peek(self):
        return self._stack.front()

    def is_empty(self):
        return self._stack.empty()

    def size(self):
        return self._stack.size()


if __name__ == "__main__":
    ss = SinglyListStack()
    print(ss)
