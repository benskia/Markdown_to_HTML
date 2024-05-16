import unittest

from htmlnode import LeafNode
from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node.", "bold")
        node2 = TextNode("This is a node with an invalid text_type.", "banana")
        leafnode = LeafNode("This is a text node.", "b")
        self.assertEqual(print(text_node_to_html_node(node)), print(leafnode))
        with self.assertRaises(Exception):
            text_node_to_html_node(node2)


class TestSplitNodesDelimiter(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
