"""
Insert value
Delete value
Count number of nodes in tree
Whether a value is in the tree
Calculate height of the tree
Binary search tree
    Determine if it is a binary search tree
    Get maximum value
    Get minimum value

"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            return self._search(root.left, data)
        return self._search(root.right, data)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root is None:
            return
        self._inorder(root.left)
        print(root.data, end=" ")
        self._inorder(root.right)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self._preorder(root.left)
        self._preorder(root.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        if root is None:
            return
        self._postorder(root.left)
        self._postorder(root.right)
        print(root.data, end=" ")

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if root is None:
            return None
        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)
        return root

    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left

        return current

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, root):
        if root is None:
            return True
        lh = self._height(root.left)
        rh = self._height(root.right)
        return (
            abs(lh - rh) <= 1
            and self._is_balanced(root.left)
            and self._is_balanced(root.right)
        )

    def is_bst(self):
        return self._is_bst(self.root, float("-inf"), float("inf"))

    def _is_bst(self, root, min_val, max_val):
        if root is None:
            return True
        if root.data < min_val or root.data > max_val:
            return False
        return self._is_bst(root.left, min_val, root.data - 1) and self._is_bst(
            root.right, root.data + 1, max_val
        )

    def lca(self, n1, n2):
        return self._lca(self.root, n1, n2)

    def _lca(self, root, n1, n2):
        if root is None:
            return None
        if root.data > n1 and root.data > n2:
            return self._lca(root.left, n1, n2)
        if root.data < n1 and root.data < n2:
            return self._lca(root.right, n1, n2)
        return root.data

    def kth_smallest(self, k):
        self.k = k
        self.kth_smallest = None
        self._kth_smallest(self.root)
        return self.kth_smallest

    def _kth_smallest(self, root):
        if root is None:
            return
        self._kth_smallest(root.left)
        self.k -= 1
        if self.k == 0:
            self.kth_smallest = root.data
            return
        self._kth_smallest(root.right)

    def kth_largest(self, k):
        self.k = k
        self.kth_largest = None
        self._kth_largest(self.root)
        return self.kth_largest

    def _kth_largest(self, root):
        if root is None:
            return
        self._kth_largest(root.right)
        self.k -= 1
        if self.k == 0:
            self.kth_largest = root.data
            return
        self._kth_largest(root.left)

    def range_sum(self, low, high):
        self.sum = 0
        self._range_sum(self.root, low, high)
        return self.sum

    def _range_sum(self, root, low, high):
        if root is None:
            return
        if root.data > low:
            self._range_sum(root.left, low, high)
        if low <= root.data <= high:
            self.sum += root.data
        if root.data < high:
            self._range_sum(root.right, low, high)

    def range_search(self, low, high):
        self.result = []
        self._range_search(self.root, low, high)
        return self.result

    def _range_search(self, root, low, high):
        if root is None:
            return
        if root.data > low:
            self._range_search(root.left, low, high)
        if low <= root.data <= high:
            self.result.append(root.data)
        if root.data < high:
            self._range_search(root.right, low, high)

    def floor(self, data):
        self.floor = None
        self._floor(self.root, data)
        return self.floor

    def _floor(self, root, data):
        if root is None:
            return
        if root.data == data:
            self.floor = root.data
            return
        if root.data > data:
            self._floor(root.left, data)
        else:
            self.floor = root.data
            self._floor(root.right, data)

    def ceil(self, data):
        self.ceil = None
        self._ceil(self.root, data)
        return self.ceil

    def _ceil(self, root, data):
        if root is None:
            return
        if root.data == data:
            self.ceil = root.data
            return
        if root.data < data:
            self._ceil(root.right, data)
        else:
            self.ceil = root.data
            self._ceil(root.left, data)

    def print_level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def print_level_order_line_by_line(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                print(node.data, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()

    def print_spiral_order(self):
        if self.root is None:
            return
        stack1 = [self.root]
        stack2 = []
        while stack1 or stack2:
            while stack1:
                node = stack1.pop()
                print(node.data, end=" ")
                if node.right:
                    stack2.append(node.right)
                if node.left:
                    stack2.append(node.left)
            while stack2:
                node = stack2.pop()
                print(node.data, end=" ")
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
        print()

    def print_vertical_order(self):
        if self.root is None:
            return
        m = {}
        queue = [(self.root, 0)]
        while queue:
            node, hd = queue.pop(0)
            if hd in m:
                m[hd].append(node.data)
            else:
                m[hd] = [node.data]
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        for k in sorted(m.keys()):
            print(*m[k])

    def print_top_view(self):
        if self.root is None:
            return
        m = {}
        queue = [(self.root, 0)]
        while queue:
            node, hd = queue.pop(0)
            if hd not in m:
                m[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        for k in sorted(m.keys()):
            print(m[k], end=" ")
        print()

    def print_bottom_view(self):
        if self.root is None:
            return
        m = {}
        queue = [(self.root, 0)]
        while queue:
            node, hd = queue.pop(0)
            m[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        for k in sorted(m.keys()):
            print(m[k], end=" ")
        print()

    def print_left_view(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == 0:
                    print(node.data, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        print()

    def print_right_view(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == n - 1:
                    print(node.data, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        print()

    def print_boundary(self):
        if self.root is None:
            return
        print(self.root.data, end=" ")
        self._print_left_boundary(self.root.left)
        self._print_leaves(self.root.left)
        self._print_leaves(self.root.right)
        self._print_right_boundary(self.root.right)
        print()

    def _print_left_boundary(self, root):
        if root is None:
            return
        if root.left:
            print(root.data, end=" ")
            self._print_left_boundary(root.left)
        elif root.right:
            print(root.data, end=" ")
            self._print_left_boundary(root.right)

    def _print_right_boundary(self, root):
        if root is None:
            return
        if root.right:
            self._print_right_boundary(root.right)
            print(root.data, end=" ")
        elif root.left:
            self._print_right_boundary(root.left)
            print(root.data, end=" ")

    def _print_leaves(self, root):
        if root is None:
            return
        self._print_leaves(root.left)
        if root.left is None and root.right is None:
            print(root.data, end=" ")
        self._print_leaves(root.right)

    def print_diagonal_order(self):
        if self.root is None:
            return
        m = {}
        self._print_diagonal_order(self.root, 0, m)
        for k in sorted(m.keys()):
            print(*m[k])

    def _print_diagonal_order(self, root, d, m):
        if root is None:
            return
        if d in m:
            m[d].append(root.data)
        else:
            m[d] = [root.data]
        self._print_diagonal_order(root.left, d + 1, m)
        self._print_diagonal_order(root.right, d, m)

    def print_diagonal_order_iterative(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            while node:
                print(node.data, end=" ")
                if node.left:
                    queue.append(node.left)
                node = node.right
        print()

    def print_diagonal_order_iterative_v2(self):
        if self.root is None:
            return
        m = {}
        queue = [(self.root, 0)]
        while queue:
            node, d = queue.pop(0)
            while node:
                if d in m:
                    m[d].append(node.data)
                else:
                    m[d] = [node.data]
                if node.left:
                    queue.append((node.left, d + 1))
                node = node.right
        for k in sorted(m.keys()):
            print(*m[k])

    def print_diagonal_order_iterative_v3(self):
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            while node:
                print(node.data, end=" ")
                if node.right:
                    stack.append(node.right)
                node = node.left
        print()
