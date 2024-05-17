import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, text_node_to_html_node


class TestInlineMarkdown(unittest.TestCase):

    def test_invalid_type(self):
        node = TextNode("invalid test", "wowee")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_delimiter_bold(self):
        node = TextNode("normal **bold** normal", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("normal ", "text"),
                TextNode("bold", "bold"),
                TextNode(" normal", "text"),
            ],
            new_nodes,
        )

    def test_delimiter_italic(self):
        node = TextNode("normal *italic* normal", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("normal ", "text"),
                TextNode("italic", "italic"),
                TextNode(" normal", "text"),
            ],
            new_nodes,
        )

    def test_delimiter_code(self):
        node = TextNode("normal `code` normal", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("normal ", "text"),
                TextNode("code", "code"),
                TextNode(" normal", "text"),
            ],
            new_nodes,
        )

    def test_multiple_splits(self):
        node = TextNode("normal **bold** normal **bold** normal", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("normal ", "text"),
                TextNode("bold", "bold"),
                TextNode(" normal ", "text"),
                TextNode("bold", "bold"),
                TextNode(" normal", "text"),
            ],
            new_nodes,
        )

    def test_multiple_words(self):
        node = TextNode(
            "normal text **bold words** normal **bold text** normal text", "text"
        )
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("normal text ", "text"),
                TextNode("bold words", "bold"),
                TextNode(" normal ", "text"),
                TextNode("bold text", "bold"),
                TextNode(" normal text", "text"),
            ],
            new_nodes,
        )