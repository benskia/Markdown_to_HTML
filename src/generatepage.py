from os import makedirs, mkdir
from os.path import dirname, exists, isfile, join, isdir

from block_markdown import (
    heading_block_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_type_heading,
    markdown_to_html_node,
)
from copystatic import get_ls


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            heading = heading_block_to_html_node(block)
            if heading.tag == "h1" and heading.children:
                return " ".join([child.value for child in heading.children])
    raise Exception(f"No h1 block founds in markdown file {markdown}.")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as f:
        from_markdown = f.read()
    with open(template_path, "r") as f:
        template_markdown = f.read()
    title = extract_title(from_markdown)
    from_html = markdown_to_html_node(from_markdown).to_html()
    template_markdown = template_markdown.replace("{{ Title }}", title)
    template_markdown = template_markdown.replace("{{ Content }}", from_html)
    makedirs(dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_markdown)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not exists(dest_dir_path):
        mkdir(dest_dir_path)
    ls = get_ls(dir_path_content)
    for item in ls:
        item_path = join(dir_path_content, item)
        if isdir(item_path):
            generate_pages_recursive(
                item_path, template_path, join(dest_dir_path, item)
            )
        elif isfile(item_path) and item_path.endswith(".md"):
            item_dest_path = join(dest_dir_path, item.replace(".md", ".html"))
            generate_page(item_path, template_path, item_dest_path)
