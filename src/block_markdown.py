def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n")
    num_lines = len(lines)
    block = []
    for i in range(num_lines):
        line = lines[i].strip()
        if line != "":
            block.append(line)
        if line == "" or i == num_lines - 1:
            blocks.append("\n".join(block))
            block = []
    return blocks
