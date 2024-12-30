class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            node = queue.pop(0)

            if node.left is None:
                node.left = Node(data)
                return
            else:
                queue.append(node.left)

            if node.right is None:
                node.right = Node(data)
                return
            else:
                queue.append(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def level_order(self):
        if self.root is None:
            return

        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def height(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0

        left_size = self.size(node.left)
        right_size = self.size(node.right)

        return 1 + left_size + right_size

    def is_full(self, node):
        if node is None:
            return True

        if node.left is None and node.right is None:
            return True

        if node.left is not None and node.right is not None:
            return self.is_full(node.left) and self.is_full(node.right)

        return False

    def is_complete(self, node, index, size):
        if node is None:
            return True

        if index >= size:
            return False

        return self.is_complete(node.left, 2 * index + 1, size) and self.is_complete(
            node.right, 2 * index + 2, size
        )

    def is_perfect(self, node, height, level=0):
        if node is None:
            return True

        if node.left is None and node.right is None:
            return height == level + 1

        if node.left is None or node.right is None:
            return False

        return self.is_perfect(node.left, height, level + 1) and self.is_perfect(
            node.right, height, level + 1
        )


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    tree = BinaryTree(root)

    print("Preorder:")
    tree.preorder(root)
    print()

    print("Inorder:")
    tree.inorder(root)
    print()

    print("Postorder:")
    tree.postorder(root)
    print()

    print("Level Order:")
    tree.level_order()
    print()

    print("Height:", tree.height(root))
    print("Size:", tree.size(root))
    print("Is Full:", tree.is_full(root))
    print("Is Complete:", tree.is_complete(root, 0, tree.size(root)))
    print("Is Perfect:", tree.is_perfect(root, tree.height(root)))
