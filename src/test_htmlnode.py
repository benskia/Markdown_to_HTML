import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        props = {"id": "test-node", "html": "https://example.com"}
        node = HTMLNode("div", "One, two, three!", None, props)
        output = 'id="test-node" html="https://example.com"'
        self.assertEqual(node.props_to_html(), output)

    def test_to_html_no_children(self):
        node = LeafNode("p", "LeafNode here!")
        output = "<p>LeafNode here!</p>"
        self.assertEqual(node.to_html(), output)

    def test_to_html_no_tag(self):
        node = LeafNode(None, "LeafNode here!")
        output = "LeafNode here!"
        self.assertEqual(node.to_html(), output)

    def test_to_html_with_children(self):
        child_node = LeafNode("p", "LeafNode here!")
        parent_node = ParentNode("section", [child_node])
        output = "<section><p>LeafNode here!</p></section>"
        self.assertEqual(parent_node.to_html(), output)

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "bold grandchild")
        child_node = ParentNode("section", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        output = "<div><section><b>bold grandchild</b></section></div>"
        self.assertEqual(parent_node.to_html(), output)

    def test_to_html_many_children(self):
        normal_child = LeafNode(None, "normal")
        bold_child = LeafNode("b", "bold")
        italic_child = LeafNode("i", "italic")
        children = [normal_child, bold_child, italic_child, normal_child]
        parent_node = ParentNode("p", children)
        output = "<p>normal<b>bold</b><i>italic</i>normal</p>"
        self.assertEqual(parent_node.to_html(), output)


if __name__ == "__main__":
    unittest.main()
