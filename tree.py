from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """ Delete the entire tree by setting the root to None """
        self.root = None

def printTree(self):
    """ Print the tree using inorder traversal """
    if self.root is not None:
        self._printInorderTree(self.root)

def _printInorderTree(self, node):
    """ Print the subtree rooted at the given node using inorder traversal """
    if node is not None:
        self._printInorderTree(node.left)
        print(str(node.data) + ' ')
        self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """ Print the subtree rooted at the given node using preorder traversal """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

def _printPostorderTree(self, node):
    """ Print the subtree rooted at the given node using postorder traversal """
    if node is not None:
        self._printPostorderTree(node.left)
        self._printPostorderTree(node.right)
        print(str(node.data) + ' ')

import unittest

class TestTreeMethods(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(2)
        self.tree.add(4)

    def test_find_existing(self):
        node = self.tree.find(3)
        self.assertEqual(node.data, 3)

    def test_find_nonexistent(self):
        node = self.tree.find(6)
        self.assertIsNone(node)

    def test_find_root(self):
        node = self.tree.find(5)
        self.assertEqual(node.data, 5)

if __name__ == '__main__':
    unittest.main()
