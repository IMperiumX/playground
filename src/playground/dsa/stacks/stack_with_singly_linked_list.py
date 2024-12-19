from playground.dsa import LinkedList, Node


class SinglyListStack:
    def __init__(self):
        self._stack = LinkedList(Node(None))


if __name__ == "__main__":
    ss = SinglyListStack()
    print(ss)
