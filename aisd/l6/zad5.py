class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.h = 1

class LeftistTree:
    def __init__(self):
        self.root = None

    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.value > b.value:
            a, b = b, a

        a.right = self.merge(a.right, b)

        if not a.left or (a.right and a.left.h < a.right.h):
            a.left, a.right = a.right, a.left

        a.h = 1 + (a.right.h if a.right else 0)

        return a

    def insert(self, value):
        new_node = Node(value)
        self.root = self.merge(self.root, new_node)

    def pop(self):
        if self.root is None:
            return None

        r = self.root
        self.root = self.merge(self.root.left, self.root.right)

        return r
