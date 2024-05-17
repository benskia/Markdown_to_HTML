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
        text_segments = old_node.split(f"![{parsed_images[0]}]({parsed_images[1]})", 1)
        num_segments = len(text_segments)
        split_nodes = []
        for i in range(num_segments):
            if text_segments[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text_segments[i], "text"))
            else:
                split_nodes.append(TextNode(text_segments[i], "image"))
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
        text_segments = old_node.split(f"![{parsed_links[0]}]({parsed_links[1]})", 1)
        num_segments = len(text_segments)
        split_nodes = []
        for i in range(num_segments):
            if text_segments[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text_segments[i], "text"))
            else:
                split_nodes.append(TextNode(text_segments[i], "link"))
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
