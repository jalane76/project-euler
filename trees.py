# Binary tree

class BinaryTreeNode:
    parent = None
    left = None
    right = None
    data = None

    def __init__(self, parent = None, data = None, left = None, right = None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right

    def add_parent(self, parent):
        self.parent = parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent
