import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_cases = [
            {"html": "http://example.com", "target": "_blank"},
            {"html": "http://onetwothree.com", "target": "that"},
        ]
        test_results = [
            'html="http://example.com" target="_blank"',
            'html="http://onetwothree.com" target="that"',
        ]
        node = HTMLNode(None, None, None, test_cases[0])
        node2 = HTMLNode(None, None, None, test_cases[1])
        self.assertEqual(node.props_to_html(), test_results[0])
        self.assertEqual(node2.props_to_html(), test_results[1])


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        test_cases = [
            {"tag": "p", "value": "How now brown cow."},
            {
                "tag": "a",
                "value": "Do you think this is a link? It is!",
                "props": {"href": "https://example.com"},
            },
        ]
        test_results = [
            "<p>How now brown cow.</p>",
            '<a href="https://example.com">Do you think this is a link? It is!</a>',
        ]
        node = LeafNode(tag=test_cases[0]["tag"], value=test_cases[0]["value"])
        node2 = LeafNode(
            tag=test_cases[1]["tag"],
            value=test_cases[1]["value"],
            props=test_cases[1]["props"],
        )
        self.assertEqual(node.to_html(), test_results[0])
        self.assertEqual(node2.to_html(), test_results[1])


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        child4 = LeafNode(value="normal text")
        child3 = LeafNode(tag="i", value="italic text")
        child2 = LeafNode(value="normal text")
        child1 = LeafNode(tag="b", value="bold text")
        parent2 = ParentNode(tag="p", children=[child2, child3])
        parent1 = ParentNode(tag="section", children=[parent2, child1, child4])

        test_result = "<section><p>normal text<i>italic text</i></p><b>bold text</b>normal text</section>"

        self.assertEqual(parent1.to_html(), test_result)


if __name__ == "__main__":
    unittest.main()
