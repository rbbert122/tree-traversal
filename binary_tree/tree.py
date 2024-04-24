from binary_tree.node import Node


class Tree:
    """Tree class for binary tree"""

    def __init__(self):
        """Constructor for Tree class"""
        self.root = None

    def get_root(self):
        """Method for get root of the tree"""
        return self.root

    def add(self, data):
        """Method for add data to the tree"""
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
        elif data < node.data and node.left is not None:
            return self._find(data, node.left)
        elif data > node.data and node.right is not None:
            return self._find(data, node.right)

    def delete_tree(self):
        """Method for delete the tree

        Returns:
            None
        """
        self.root = None

    def print_tree(self):
        """Method for print the tree

        Returns:
            None
        """
        if self.root is not None:
            self._print_inorder_tree(self.root)

    def _print_inorder_tree(self, node):
        """Method for print the tree in inorder

        Args:
            node (Node): start node

        Returns:
            None
        """
        if node is not None:
            self._print_inorder_tree(node.left)
            print(str(node.data) + " ")
            self._print_inorder_tree(node.right)

    def _print_preorder_tree(self, node):
        """Method for print the tree in preorder

        Args:
            node (Node): start node

        Returns:
            None
        """
        if node is not None:
            print(str(node.data) + " ")
            self._print_preorder_tree(node.left)
            self._print_preorder_tree(node.right)

    def _print_postorder_tree(self, node):
        """Method for print the tree in postorder

        Args:
            node (Node): start node

        Returns:
            None
        """
        if node is not None:
            self._print_postorder_tree(node.left)
            self._print_postorder_tree(node.right)
            print(str(node.data) + " ")
