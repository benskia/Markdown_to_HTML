import re

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
