import unittest

from htmlnode import LeafNode
from textnode import TextNode, split_nodes_delimiter, text_node_to_html_node


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
    def test_eq(self):
        node1 = TextNode("normal `code` normal", "text")
        node2 = TextNode("bold *italic* bold", "bold")
        node3 = TextNode("normal **invalid normal", "text")
        node4 = TextNode("normal **bold** normal", "text")
        input = [node1, node2, node3, node4]

        sc1 = TextNode("normal ", "text")
        sc2 = TextNode("code", "code")
        sc3 = TextNode(" normal", "text")
        code_output = [sc1, sc2, sc3, node2, node3]

        self.assertEqual(split_nodes_delimiter(input, "`", "code"), code_output)
        self.assertEqual(split_nodes_delimiter(input, "*", "italic"), input)
        with self.assertRaises(Exception):
            split_nodes_delimiter(input, "**", "bold")


if __name__ == "__main__":
    unittest.main()
