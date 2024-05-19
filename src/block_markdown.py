import re

from htmlnode import HTMLNode, LeafNode, ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n")
    num_lines = len(lines)
    block = []
    for i in range(num_lines):
        line = lines[i].strip()
        if line != "":
            block.append(line)
        end_of_block = (line == "" or i == num_lines - 1) and len(block) > 0
        if end_of_block:
            blocks.append("\n".join(block))
            block = []
    return blocks


def block_to_block_type(block):
    if re.match(r"^#{1,6} .*", block):
        return block_type_heading
    if re.match(r"^```.*```$", block):
        return block_type_code
    if all([re.match(r"^> .*$", line) for line in block.split("\n")]):
        return block_type_quote
    if all([re.match(r"^[*-] .*$", line) for line in block.split("\n")]):
        return block_type_ulist
    lines = block.split("\n")
    if all([re.match(rf"^{i+1}. .*$", lines[i]) for i in range(len(lines))]):
        return block_type_olist
    return block_type_paragraph


def block_to_htmlnode_error(block, block_type):
    if block_to_block_type(block) != block_type:
        return f"Tried to use non-{block_type} block to create {block_type} html node."
    return None


def heading_block_to_html_node(block):
    err = block_to_htmlnode_error(block, block_type_heading)
    if err == None:
        heading_rank = 0
        while block[heading_rank] != " ":
            heading_rank += 1
        return LeafNode(f"h{heading_rank}", f"{block[heading_rank:]}")
    else:
        raise Exception(err)


def code_block_to_html_node(block):
    err = block_to_htmlnode_error(block, block_type_code)
    if err == None:
        return LeafNode(f"code", f"{block[3:-3]}")
    else:
        raise Exception(err)


def quote_block_to_html_node(block):
    err = block_to_htmlnode_error(block, block_type_quote)
    if err == None:
        lines = block.split("\n")
        quote = "\n".join([line.lstrip("> ") for line in lines])
        return LeafNode(f"blockquote", f"{quote}")
    else:
        raise Exception(err)


def ulist_block_to_html_node(block):
    err = block_to_htmlnode_error(block, block_type_ulist)
    if err == None:
        lines = block.split("\n")
        cleaned_lines = [line.lstrip("* ").lstrip("- ") for line in lines]
        list_items = [LeafNode("li", line) for line in cleaned_lines]
        return ParentNode("ul", list_items)
    else:
        raise Exception(err)
