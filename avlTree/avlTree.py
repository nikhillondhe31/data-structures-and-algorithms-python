class Node:

    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0


class AVlTree:
    def __init__(self):
        # Access the root node exclusively
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # if less than root node move to left
        if data < node.data:
            if node.left_node is None:
                node.left_node = Node(data, node)
                # calculate height on every insertion

            else:
                self.insert_node(data, node.left_node)

        else:
            if node.right_node is None:
                node.right_node = Node(data, node)
            else:
                self.insert_node(data, node.right_node)


if __name__ == '__main__':
    avl = AVlTree()
    avl.insert(10)
    avl.insert(12)
    avl.insert(9)

    print("root node: ", avl.root.data)
    print("left node: ", avl.root.left_node.data)
    print("right node: ", avl.root.right_node.data)
