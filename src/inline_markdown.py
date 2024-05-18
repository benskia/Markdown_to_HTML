import re
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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        parsed_images = extract_markdown_images(old_node.text)
        if len(parsed_images) == 0:
            new_nodes.append(old_node)
            continue
        for parsed_image in parsed_images:
            if len(parsed_image) < 2:
                continue
            split_nodes = []
            alt = parsed_image[0]
            url = parsed_image[1]
            text_segments = old_node.text.split(f"![{alt}]({url})", 1)
            first = text_segments[0]
            last = text_segments[1]
            if first != "":
                split_nodes.append(TextNode(first, "text"))
            split_nodes.append(TextNode(alt, "image", url))
            if last != "":
                split_nodes.append(TextNode(last, "text"))
            new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        parsed_links = extract_markdown_links(old_node.text)
        if len(parsed_links) == 0:
            new_nodes.append(old_node)
            continue
        for parsed_link in parsed_links:
            if len(parsed_link) < 2:
                continue
            split_nodes = []
            link_text = parsed_link[0]
            url = parsed_link[1]
            text_segments = old_node.text.split(f"[{link_text}]({url})", 1)
            first = text_segments[0]
            last = text_segments[1]
            if first != "":
                split_nodes.append(TextNode(first, "text"))
            split_nodes.append(TextNode(link_text, "link", url))
            if last != "":
                split_nodes.append(TextNode(last, "text"))
            new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    parsed_images = re.findall(pattern, text)
    return parsed_images


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    parsed_links = re.findall(pattern, text)
    return parsed_links
