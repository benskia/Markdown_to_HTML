import re

from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes

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


def heading_block_to_html_node(block):
    heading_rank = 0
    while block[heading_rank] != " ":
        heading_rank += 1
    return LeafNode(f"h{heading_rank}", f"{block[heading_rank:]}")


def code_block_to_html_node(block):
    return LeafNode(f"code", f"{block[3:-3]}")


def quote_block_to_html_node(block):
    lines = block.split("\n")
    quote = "\n".join([line.lstrip("> ") for line in lines])
    return LeafNode(f"blockquote", f"{quote}")


def ulist_block_to_html_node(block):
    lines = block.split("\n")
    cleaned_lines = [line.lstrip("* ").lstrip("- ") for line in lines]
    list_items = [LeafNode("li", line) for line in cleaned_lines]
    return ParentNode("ul", list_items)


def olist_block_to_html_node(block):
    lines = block.split("\n")
    cleaned_lines = [re.sub(r"\d+. ", "", line, count=1) for line in lines]
    list_items = [LeafNode("li", line) for line in cleaned_lines]
    return ParentNode("ol", list_items)


def paragraph_block_to_html_node(block):
    text_nodes = text_to_textnodes(block)
    return ParentNode("p", text_nodes)


def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            children.append(heading_block_to_html_node(block))
        if block_type == block_type_code:
            children.append(code_block_to_html_node(block))
        if block_type == block_type_quote:
            children.append(quote_block_to_html_node(block))
        if block_type == block_type_ulist:
            children.append(ulist_block_to_html_node(block))
        if block_type == block_type_olist:
            children.append(olist_block_to_html_node(block))
        if block_type == block_type_paragraph:
            children.append(paragraph_block_to_html_node(block))
    return ParentNode("div", children)
