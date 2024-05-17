from htmlnode import LeafNode


text_to_html_types = {
    "text": None,
    "bold": "b",
    "italic": "i",
    "code": "code",
    "link": "a",
    "image": "img",
}


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

    tag = text_to_html_types.get(text_node.text_type, "invalid")
    if tag == "invalid":
        raise Exception(f"Invalid text type: {text_node.text_type}.")

    if tag == "a":
        return LeafNode(tag, text_node.text, {"href": text_node.url})
    if tag == "img":
        return LeafNode(tag, "", {"src": text_node.url, "alt": text_node.text})

    return LeafNode(tag, text_node.text)


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
        delimiter_text_type = delimiter_text_types.get(delimiter, "invalid")
        if delimiter_text_type == "invalid":
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

        split_nodes = []
        # Text targeted by delimiter will always be odd, because the delimited
        # text is always nested within its parent TextNode.
        for i in range(num_segments):
            # An empty string likely indicates we split on adjacent delimiters.
            if text_segments[i] == "":
                raise Exception(
                    "Encountered an empty segment: tried to split on adjacent delimiters."
                )
            if i % 2 == 0:
                split_nodes.append(TextNode(text_segments[i], text_type))
            else:
                split_nodes.append(TextNode(text_segments[i], delimiter_text_type))
        new_nodes.extend(split_nodes)

    return new_nodes
