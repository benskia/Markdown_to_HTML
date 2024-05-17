import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("These nodes are the same.", "bold")
        node2 = TextNode("These nodes are the same.", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("These nodes have different types.", "bold")
        node2 = TextNode("These nodes have different types.", "text")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("These nodes have different text!", "text")
        node2 = TextNode("These nodes have different text...", "text")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("These nodes have the same url.", "code", "https://example.com")
        node2 = TextNode(
            "These nodes have the same url.", "code", "https://example.com"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        input = TextNode("This tests repr!", "link", "https://example.com")
        output = "TextNode(This tests repr!, link, https://example.com)"
        self.assertEqual(repr(input), output)


if __name__ == "__main__":
    unittest.main()
