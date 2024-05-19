import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_link,
    text_type_code,
)


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("These nodes are the same.", text_type_bold)
        node2 = TextNode("These nodes are the same.", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("These nodes have different types.", text_type_bold)
        node2 = TextNode("These nodes have different types.", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("These nodes have different text!", text_type_text)
        node2 = TextNode("These nodes have different text...", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode(
            "These nodes have the same url.", text_type_code, "https://example.com"
        )
        node2 = TextNode(
            "These nodes have the same url.", text_type_code, "https://example.com"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        input = TextNode("This tests repr!", text_type_link, "https://example.com")
        output = "TextNode(This tests repr!, link, https://example.com)"
        self.assertEqual(repr(input), output)


if __name__ == "__main__":
    unittest.main()
