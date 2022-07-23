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
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
                # handle violations
                self.handle_violation(node)

            else:
                self.insert_node(data, node.left_node)

        else:
            if node.right_node is None:
                node.right_node = Node(data, node)
            else:
                self.insert_node(data, node.right_node)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return

        # check if the node is less or greater than the root node
        elif data < node.data:
            # recursively check the left sub-tree of the root
            self.remove_node(data, node.left_node)

        elif data > node.data:
            # recursively check the right sub-tree of the root node
            self.remove_node(data, node.right_node)

        else:
            # we have found the node to be deleted
            # case 1: The node to be deleted is the leaf node(the node does not have a left or right child)
            if node.right_node is None and node.left_node is None:
                # It is a leaf node
                # make the parent of the leaf node point to None
                parent = node.parent
                # check if it is right_node or left_node
                if parent:
                    if parent.left_node == node and parent:
                        print("removing leaf node. That is left node of the root")
                        parent.left_node = None
                    elif parent.right_node == node and parent:
                        print("removing leaf node. That is right node of the root")
                        parent.right_node = None
                else:
                    print("removing the root node")
                    self.root = None
                del node
                # after every deletion we have to check whether the AVL properties are violated
                self.handle_violation(parent)

            # Case2: It has a single right child node
            elif node.right_node and not node.left_node:
                print("removing node with single right child...")
                # removing node with single right child
                parent = node.parent

                # determine whether the node to be removed is the parent's left node
                if parent and parent.left_node == node:
                    # update the parent's left node to node's right child
                    parent.left_node = node.right_node

                # determine whether the node to be removed is the parent's right node
                elif parent and parent.right_node == node:
                    # update the parent's right node to the node's right node
                    parent.right_node = node.right_node

                else:
                    # the parent is None, that means the node to be removed is root node
                    self.root = node.right_node

                node.right_node.parent = parent

                del node

                self.handle_violation(parent)

            # Case3: It has a single left child node
            elif node.left_node and not node.right_node:
                print("removing node with single left...")
                # removing node with single right child
                parent = node.parent

                # determine whether the node to be removed is the parent's left node
                if parent and parent.left_node == node:
                    # update the parent's left node to node's right child
                    parent.left_node = node.left_node

                # determine whether the node to be removed is the parent's right node
                elif parent and parent.right_node == node:
                    # update the parent's right node to the node's right node
                    parent.right_node = node.left_node

                else:
                    # the parent is None, that means the node to be removed is root node
                    self.root = node.left_node

                node.left_node.parent = parent

                del node

                self.handle_violation(parent)

            # Case4: Final case the node have 2 children
            else:
                print("Removing node with 2 children...")
                predecessor = self.get_predecessor(node.left_node)

                # swap the node and the predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            self.get_predecessor(node.right_node)
        return node

    def calc_height(self, node):
        # this is when the node is a NULL
        if not node:
            return -1
        return node.height

    def handle_violation(self, node):
        # check the nodes from the node we have inserted up to the root node
        while node is not None:
            node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node))+1
            self.violation_helper(node)
            # whenever we settle a violation (rotations) it may happen that it
            # violates the AVL properties in other part of the tree
            node = node.parent

    # checks whether the subtree is balanced with root node = node
    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        # Tree can be left left heavy or left right heavy
        # balance is greater than 1: left right heavy situation. left rotation on parent + right rotation on grandparent
        if balance > 1:
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)

            self.rotate_right(node)

        if balance < -1:
            if self.calculate_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)
            self.rotate_left(node)
# implement rotate right and rotate left

    def calculate_balance(self, node):
        if not node:
            return 0

        return self.calc_height(node.left_node) - self.calc_height(node.right_node)


if __name__ == '__main__':
    avl = AVlTree()
    avl.insert(10)
    avl.insert(8)
    avl.insert(9)
    avl.insert(1)

    # print("root node: ", avl.root.data)
    print("left node: ", avl.root.left_node.data)
    # print("right node: ", avl.root.right_node.data)

    print(avl.remove(8))

    # print("root node: ", avl.root.data)
    print("left node: ", avl.root.left_node.data)
    print("right node: ", avl.root.left_node.right_node.data)
