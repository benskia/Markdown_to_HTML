import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)
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

    def test_image_extraction(self):
        input = "Text with an ![image](https://image.source) embedded image."
        output = [("image", "https://image.source")]
        self.assertEqual(extract_markdown_images(input), output)

    def test_link_extraction(self):
        input = "Text with a [link](https://example.com) link."
        output = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(input), output)

    def test_image_splitter(self):
        node = TextNode(
            "Text with an ![image](https://image.source) embedded image.", "text"
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text with an ", "text"),
                TextNode("image", "image", "https://image.source"),
                TextNode(" embedded image.", "text"),
            ],
            new_nodes,
        )

    def test_link_splitter(self):
        node = TextNode("Text with a [link](https://example.com) link.", "text")
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text with a ", "text"),
                TextNode("link", "link", "https://example.com"),
                TextNode(" link.", "text"),
            ],
            new_nodes,
        )
