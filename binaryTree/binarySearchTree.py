class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self.insert(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        else:
            if node.right_node:
                self.insert(data, node.right_node)
            else:
                node.right_node = Node(data, node)