from os.path import dirname

from block_markdown import (
    heading_block_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_type_heading,
    markdown_to_html_node,
)


def extract_title(markdown):
    with open(markdown, "r") as f:
        blocks = markdown_to_blocks(f.read())
        for block in blocks:
            if block_to_block_type(block) == block_type_heading:
                heading = heading_block_to_html_node(block)
                if heading.tag == "h1":
                    return heading.value
    raise Exception(f"No h1 block founds in markdown file {markdown}.")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as f:
        from_markdown = f.read()
    with open(template_path, "r") as f:
        template_markdown = f.read()
    from_html = markdown_to_html_node(from_markdown).to_html()
    title = extract_title(from_markdown)
    if not title:
        return
    template_markdown = template_markdown.replace("{{ Title }}", title)
    template_markdown = template_markdown.replace("{{ Content }}", from_html)
    working_directory = dirname(dest_path)
