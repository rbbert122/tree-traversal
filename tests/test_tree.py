import unittest
from binary_tree.tree import Tree


class TestFindMethod(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()

        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)

    def test_find_existing_node(self):
        node = self.tree._find(10, self.tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 10)

    def test_find_non_existing_node(self):
        node = self.tree._find(20, self.tree.root)
        self.assertIsNone(node)

    def test_find_existing_node_in_left_subtree(self):
        node = self.tree._find(5, self.tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

    def test_find_existing_node_in_right_subtree(self):
        node = self.tree._find(15, self.tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 15)


if __name__ == "__main__":
    unittest.main()
