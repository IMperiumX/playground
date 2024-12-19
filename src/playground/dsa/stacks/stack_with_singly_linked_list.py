from playground.dsa import LinkedList, Node, StackADT


class SinglyListStack(StackADT):
    def __init__(self):
        self._stack = LinkedList(Node(None))

    def __str__(self):
        return str(self._stack)


if __name__ == "__main__":
    ss = SinglyListStack()
    print(ss)
