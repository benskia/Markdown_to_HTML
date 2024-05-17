from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # We're only splitting TextNodes of type "text".
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        text_segments = old_node.text.split(delimiter)
        num_segments = len(text_segments)
        # An even number of segments indicates solo delimiters were encountered.
        if num_segments % 2 == 0:
            raise Exception("Invalid markdown: unpaired delimiter encountered.")
        split_nodes = []
        # Text targeted by delimiter will always be odd, because the delimited
        # text is always nested within its parent TextNode.
        for i in range(num_segments):
            # An empty string likely indicates we split on adjacent delimiters.
            if text_segments[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text_segments[i], "text"))
            else:
                split_nodes.append(TextNode(text_segments[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
