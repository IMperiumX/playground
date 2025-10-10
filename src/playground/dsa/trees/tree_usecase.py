# Of course. Here is a comprehensive Python application that implements and demonstrates the key concepts from the chapter summary.

# This single, runnable script includes:
# 1.  A concrete `LinkedBinaryTree` implementation.
# 2.  Implementations of all four major traversal algorithms.
# 3.  A demonstration of building a tree to represent a file system.
# 4.  A practical application of the **Euler Tour** using the **Template Method Pattern** to create a labeled, indented directory listing.
# 5.  A full implementation of the **Expression Tree** case study, including building a tree from a string and evaluating it.

# Each section is clearly commented to explain how the code relates to the theoretical concepts.

#
# --- Core Data Structures (from Sections 8.2 and 8.3) ---
#
# We implement a LinkedBinaryTree, which is a concrete class for the
# Binary Tree ADT. It uses a linked structure with _Node objects.
#


class LinkedBinaryTree:
    """A linked representation of a binary tree structure."""

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""

        __slots__ = "_element", "_parent", "_left", "_right"  # space optimization

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    # -------------------------- nested Position class --------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    # ------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # -------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # -------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # -------------------------- nonpublic update methods --------------------------
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position."""
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e."""
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e."""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    #
    # --- Tree Traversal Implementations (from Section 8.4) ---
    #
    # These methods generate iterations of the tree's positions. We use
    # recursion with Python's 'yield' keyword to create generators.
    #

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.__len__() == 0:
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p
        if self.left(p) is not None:
            for other in self._subtree_preorder(self.left(p)):
                yield other
        if self.right(p) is not None:
            for other in self._subtree_preorder(self.right(p)):
                yield other

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.__len__() == 0:
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_postorder(self.left(p)):
                yield other
        if self.right(p) is not None:
            for other in self._subtree_postorder(self.right(p)):
                yield other
        yield p

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.__len__() == 0:
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.__len__() == 0:
            from collections import deque

            q = deque([self.root()])
            while len(q) > 0:
                p = q.popleft()
                yield p
                if self.left(p) is not None:
                    q.append(self.left(p))
                if self.right(p) is not None:
                    q.append(self.right(p))


#
# --- Application 1: File System Tree and Traversal Demonstration ---
#


def build_file_system_tree():
    """Builds and returns a LinkedBinaryTree representing a file system."""
    print("Building a sample file system tree...")
    fs_tree = LinkedBinaryTree()
    root = fs_tree._add_root("/user/rt/courses/")

    cs016 = fs_tree._add_left(root, "cs016/")
    cs252 = fs_tree._add_right(root, "cs252/")

    # cs016 subtree
    fs_tree._add_left(cs016, "grades")
    homeworks = fs_tree._add_right(cs016, "homeworks/")
    fs_tree._add_left(homeworks, "hw1")
    fs_tree._add_right(homeworks, "hw2")

    # cs252 subtree
    projects = fs_tree._add_left(cs252, "projects/")
    fs_tree._add_right(cs252, "private.txt")
    fs_tree._add_left(projects, "project1")
    demos = fs_tree._add_right(projects, "demos/")
    fs_tree._add_left(demos, "market")

    return fs_tree


#
# --- Application 2: The Euler Tour Framework (from Section 8.4.6) ---
#
# This demonstrates the Template Method Pattern. We create a generic tour
# framework, then subclass it to create a specific, useful application.
#


class EulerTour:
    """
    Abstract base class for performing an Euler tour of a tree.
    Subclasses can override hook methods to customize the tour's behavior.
    """

    def __init__(self, tree):
        self._tree = tree

    def execute(self):
        """Perform the tour and return a result (if any)."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])  # start recursion

    def _tour(self, p, d, path):
        """
        Perform tour of subtree rooted at p.
        p: position of current node
        d: depth of p in the tree
        path: list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)  # add new index for children of p
        # In a general tree, we would loop through all children.
        # In our binary tree, we check left then right.
        if self._tree.left(p) is not None:
            results.append(self._tour(self._tree.left(p), d + 1, path))
            path[-1] += 1
        if self._tree.right(p) is not None:
            results.append(self._tour(self._tree.right(p), d + 1, path))
        path.pop()
        return self._hook_postvisit(p, d, path, results)

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class PreorderLabeledTour(EulerTour):
    """
    A specific application of EulerTour that prints a labeled, indented
    preorder listing of the tree's contents. This demonstrates how to
    customize the tour by overriding a hook.
    """

    def _hook_previsit(self, p, d, path):
        # Create label like "2.1.3"
        label = ".".join(str(j + 1) for j in path)
        if not label:
            label = "ROOT"

        print(f"{'  ' * d}{label}: {p.element()}")


#
# --- Application 3: Case Study - Expression Tree (from Section 8.5) ---
#
# A specialized tree for representing and evaluating arithmetic expressions.
#


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree.
        In a single-parameter call, token is a literal value.
        In a three-parameter call, token is an operator, and left/right are subtrees.
        """
        super().__init__()
        if not isinstance(token, str):
            raise TypeError("Token must be a string")

        if left is None and right is None:
            self._add_root(token)  # leaf node
        else:
            if not (
                isinstance(left, ExpressionTree) and isinstance(right, ExpressionTree)
            ):
                raise TypeError(
                    "left and right subtrees must be ExpressionTree instances"
                )
            root = self._add_root(token)  # operator node
            # Attach subtrees
            if len(left) > 0:
                left_root_node = left._root
                self._root._left = left_root_node
                left_root_node._parent = self._root
            if len(right) > 0:
                right_root_node = right._root
                self._root._right = right_root_node
                right_root_node._parent = self._root

    def __str__(self):
        """Return string representation of the expression (parenthesized)."""
        # This is an inorder-style traversal for printing
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return "".join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append parenthesized representation of subtree to result list."""
        if self.num_children(p) > 0:
            result.append("(")
        if self.left(p) is not None:
            self._parenthesize_recur(self.left(p), result)

        result.append(str(p.element()))

        if self.right(p) is not None:
            self._parenthesize_recur(self.right(p), result)
        if self.num_children(p) > 0:
            result.append(")")

    def evaluate(self):
        """Return the numeric result of the expression."""
        # This is a postorder traversal for evaluation
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.num_children(p) == 0:  # a leaf
            return float(p.element())
        else:
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            op = p.element()
            if op == "+":
                return left_val + right_val
            if op == "-":
                return left_val - right_val
            if op == "*":
                return left_val * right_val
            if op == "/":
                return left_val / right_val


def build_expression_tree(tokens):
    """Returns an ExpressionTree from a tokenized postfix expression."""
    S = []  # We use a list as a stack
    for t in tokens:
        if t in "+-*/":
            # t is an operator
            S.append(t)
        elif t != "(" and t != ")":
            # t is a literal
            S.append(ExpressionTree(t))
        elif t == ")":
            # end of a subexpression
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()


# --- Main Execution Block ---

if __name__ == "__main__":
    # --- DEMONSTRATION 1: TRAVERSALS ---
    print("=" * 60)
    print("DEMO 1: Building a File System Tree and Running Traversals")
    print("=" * 60)
    fs = build_file_system_tree()

    print("\n--- Preorder Traversal (like 'ls -R' or a table of contents) ---")
    print([p.element() for p in fs.preorder()])

    print("\n--- Postorder Traversal (useful for calculating total size) ---")
    print([p.element() for p in fs.postorder()])

    print("\n--- Inorder Traversal (less common for file systems) ---")
    print([p.element() for p in fs.inorder()])

    print("\n--- Breadth-First Traversal (visits level by level) ---")
    print([p.element() for p in fs.breadthfirst()])

    # --- DEMONSTRATION 2: EULER TOUR ---
    print("\n" + "=" * 60)
    print("DEMO 2: Euler Tour to Create a Labeled Directory Listing")
    print("=" * 60)
    # The PreorderLabeledTour customizes the generic EulerTour
    # to produce a formatted, indented output.
    labeled_tour = PreorderLabeledTour(fs)
    labeled_tour.execute()

    # --- DEMONSTRATION 3: EXPRESSION TREE ---
    print("\n" + "=" * 60)
    print("DEMO 3: Expression Tree Case Study")
    print("=" * 60)

    expression_string = "(((5 + 2) * (8 - 3)) / 4)"
    print(f"Building an expression tree for: {expression_string}")

    # Tokenize the string (simple split for this example)
    tokens = expression_string.replace("(", "( ").replace(")", " )").split()
    print(f"Tokenized input: {tokens}")

    # Build the tree using the stack-based algorithm
    expr_tree = build_expression_tree(tokens)

    print("\n--- String Representation (Inorder Traversal) ---")
    # The __str__ method uses an inorder-style traversal to reconstruct the string
    print(f"Parenthesized string: {expr_tree}")

    print("\n--- Evaluation (Postorder Traversal) ---")
    # The evaluate() method uses a postorder traversal
    result = expr_tree.evaluate()
    print(f"Evaluation result: {result}")
    print("Correct answer is (7 * 5) / 4 = 8.75")
