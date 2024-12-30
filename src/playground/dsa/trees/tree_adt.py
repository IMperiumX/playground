import abc


class TreeADT(meta=abc.ABCMeta):
    class Position(meta=abc.ABCMeta):
        @abc.abstractmethod
        def element(self):
            pass

        @abc.abstractmethod
        def __eq__(self, other):
            pass

        def __ne__(self, other):
            return not (self == other)

    def __len__(self):
        return self.size()

    def __contains__(self, value):
        return self.search(value)

    def __iter__(self):
        return self.inorder()

    @abc.abstractmethod
    def insert(self, value):
        pass

    @abc.abstractmethod
    def delete(self, value):
        pass

    @abc.abstractmethod
    def search(self, value):
        pass

    @abc.abstractmethod
    def inorder(self):
        pass

    @abc.abstractmethod
    def preorder(self):
        pass

    @abc.abstractmethod
    def postorder(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}({', '.join(str(i) for i in self)})"
