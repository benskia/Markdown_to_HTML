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
    text_type_codes = {
        "*": "italic",
        "**": "bold",
        "`": "code",
    }

    new_nodes = []
    for node in old_nodes:
        # We're only splitting raw text.
        if node.text_type != "text":
            new_nodes.append(node)
            continue

        text_segments = node.text.split(delimiter)
        num_segments = len(text_segments)

        # A size of 1 indicates no split took place.
        if num_segments == 1:
            new_nodes.append(node)
            continue

        # An even size indicates an odd number of delimiters were encountered - no matching, closing delimiter.
        if num_segments % 2 == 0:
            raise Exception(
                "Encountered an even number of segments after splitting, indicating a delimiter without a matching, closing delimiter."
            )
        for i in range(num_segments):
            if i % 2 == 0:
                new_nodes.append(TextNode(text_segments[i], text_type))
            else:
                new_nodes.append(
                    TextNode(text_segments[i], text_type_codes.get(delimiter))
                )

    return new_nodes
