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
        test_nodes = [
            TextNode("", "link"),
            TextNode("normal text **bold text** normal text", None),
            TextNode("bold text *italic text* bold text", "bold"),
            TextNode("italic text *invalid markdown text italic text", "italic"),
        ]

        result1 = [
            TextNode("", "link"),
            TextNode("normal text ", None),
            TextNode("bold text", "bold"),
            TextNode(" normal text", None),
            TextNode("bold text *italic text* bold text", "bold"),
            TextNode("italic text *invalid markdown text italic text", "italic"),
        ]
        result2 = [
            TextNode("", "link"),
            TextNode("bold text ", "bold"),
            TextNode("italic text", "italic"),
            TextNode(" bold text", "bold"),
            TextNode("bold text *italic text* bold text", "bold"),
            TextNode("italic text *invalid markdown text italic text", "italic"),
        ]
        result3 = [
            TextNode("", "link"),
            TextNode("normal text **bold text** normal text", None),
            TextNode("bold text *italic text* bold text", "bold"),
            TextNode("italic text *invalid markdown text italic text", "italic"),
        ]

        input1 = split_nodes_delimiter(test_nodes, "**", None)
        self.assertEqual(input1, result1)
        input2 = split_nodes_delimiter(test_nodes, "*", "bold")
        self.assertEqual(input1, result1)


if __name__ == "__main__":
    unittest.main()
