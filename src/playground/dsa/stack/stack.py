class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass


class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return bool(self.stack)

    def pop(self):
        if not self.stack:
            raise StackUnderflowError
        return self.pop()

    def push(self, data):
        if self.is_full():
            raise StackOverflowError
        self.stack.append(data)

    def peek(self):
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def is_full(self):
        return self.size() >= self.limit
        try:
            self.push(0)
        except StackOverflowError:
            return True
        return False

    def size(self):
        return len(self.stack)

    def __contains__(self, item):
        return item in self.stack
