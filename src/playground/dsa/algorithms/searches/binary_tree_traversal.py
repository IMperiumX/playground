import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(tree: TreeNode):
    if not tree:
        return

    print(tree.data, end=" ")
    pre_order(tree.left)
    pre_order(tree.right)


def in_order(tree: TreeNode):
    if not tree:
        return

    in_order(tree.left)
    print(tree.data, end=" ")
    in_order(tree.right)


def post_order(tree: TreeNode):
    if not tree:
        return

    post_order(tree.left)
    post_order(tree.right)
    print(tree.data, end=" ")


def level_order(tree: TreeNode):
    if not tree:
        return

    q = queue.Queue()
    q.put(tree)

    while not q.empty():
        cur = q.get()
        print(cur.data, end=" ")
        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)


def level_order_by_level(tree: TreeNode):
    if not tree:
        return

    q = queue.Queue()
    q.put(tree)

    while not q.empty():
        n = q.qsize()
        while n > 0:
            cur = q.get()
            print(cur.data, end=" ")
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
            n -= 1
        print()


def pre_order_iter(tree: TreeNode):
    stack = []
    stack.append(tree)

    while stack:
        cur = stack.pop()
        print(cur.data, end=" ")
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


def in_order_iter(tree: TreeNode):
    stack = []
    cur = tree

    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print(cur.data, end=" ")
            cur = cur.right


def post_order_iter(tree: TreeNode):
    stack = []
    stack.append(tree)
    out = []

    while stack:
        cur = stack.pop()
        out.append(cur.data)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)

    while out:
        print(out.pop(), end=" ")


"""
    1
  2   3
 4 5 6 7
"""

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    print("Pre-order traversal:", end=" ")
    pre_order(tree)
    print("\nIn-order traversal:", end=" ")
    in_order(tree)
    print("\nPost-order traversal:", end=" ")
    post_order(tree)

    print("\nLevel-order traversal:", end=" ")
    level_order(tree)
    print()

    print("Level-order traversal by level:")
    level_order_by_level(tree)

    print("Pre-order traversal (iterative):", end=" ")
    pre_order_iter(tree)

    print("\nIn-order traversal (iterative):", end=" ")
    in_order_iter(tree)

    print("\nPost-order traversal (iterative):", end=" ")
    post_order_iter(tree)
