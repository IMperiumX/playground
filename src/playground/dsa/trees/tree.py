from .tree_adt import TreeADT


class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []


class Tree(TreeADT):
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None
