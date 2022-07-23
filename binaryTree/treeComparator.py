from binaryTree.binarySearchTree import BinarySearchTree


class TreeComparator:
    def compare(self, node1, node2):
        # check the base case (so these node may be the nodes of a leaf node
        # node1 may be a none or node 2 may be a none
        if not node1 or not node2:
            return node1 == node2

        # we have to check the values in the nodes
        if node1.data is not node2.data:
            return False

        # check all the left and right subtrees (children) recursively
        return self.compare(node1.left_node, node2.left_node) and \
               self.compare(node1.right_node, node2.right_node)


if __name__ == '__main__':
    bst1 = BinarySearchTree()
    bst1.insert(10)
    bst1.insert(5)
    bst1.insert(8)
    bst1.insert(12)
    bst1.insert(-5)

    bst2 = BinarySearchTree()
    bst2.insert(10)
    bst2.insert(5)
    bst2.insert(8)
    bst2.insert(10)
    bst2.insert(-5)

    treecomparator = TreeComparator()

    print(treecomparator.compare(bst1.root, bst2.root))
