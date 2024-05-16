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
    tags = {
        "text": None,
        "bold": "b",
        "italic": "i",
        "code": "code",
        "link": "a",
        "image": "img",
    }

    text_tag = tags.get(text_node.text_type, "not found")
    if text_tag == "not found":
        raise Exception(f"Unkown node text_type: {text_node.text_type}.")

    text_props = {"href": text_node.url} if text_tag == "a" else None

    return LeafNode(tag=text_tag, value=text_node.text, props=text_props)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if len(old_nodes) == 0:
        raise Exception("Node input was empty.")

    delimiter_text_types = {
        "*": "italic",
        "**": "bold",
        "`": "code",
    }

    new_nodes = []
    for node in old_nodes:
        # We're only splitting "text_type" TextNodes.
        if node.text_type != text_type:
            new_nodes.append(node)
            continue
        # Is the delimiter valid?
        text_type_code = delimiter_text_types.get(delimiter, "invalid")
        if text_type_code == "invalid":
            new_nodes.append(node)
            continue

        text_segments = node.text.split(delimiter)
        num_segments = len(text_segments)
        # A single segment indicates no split took place.
        if num_segments == 1:
            new_nodes.append(node)
            continue
        # An even number of segments indicates solo delimiters were encountered.
        if num_segments % 2 == 0:
            new_nodes.append(node)
            continue

    return new_nodes
