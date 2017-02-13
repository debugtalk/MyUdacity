class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        self.traversal = []

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        self.preorder_print(self.root)
        return "-".join(self.traversal)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True

            if self.preorder_search(start.left, find_val):
                return True

            if self.preorder_search(start.right, find_val):
                return True

        return False

    def preorder_print(self, start):
        """Helper method - use this to create a
        recursive print solution."""
        if start is None:
            return
        self.traversal.append(str(start.value))
        self.preorder_print(start.left)
        self.preorder_print(start.right)


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
assert tree.search(4) is True
# Should be False
assert tree.search(6) is False

# Test print_tree
# Should be 1-2-4-5-3
assert tree.print_tree() == "1-2-4-5-3"
