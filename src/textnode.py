from htmlnode import LeafNode


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    text_to_html_types = {
        "text": None,
        "bold": "b",
        "italic": "i",
        "code": "code",
        "link": "a",
        "image": "img",
    }
    tag = text_to_html_types.get(text_node.text_type, "invalid")
    if tag == "invalid":
        raise Exception(f"Invalid text type: {text_node.text_type}.")
    if tag == "a":
        return LeafNode(tag, text_node.text, {"href": text_node.url})
    if tag == "img":
        return LeafNode(tag, "", {"src": text_node.url, "alt": text_node.text})
    return LeafNode(tag, text_node.text)
