from os.path import exists
from shutil import rmtree
from generatepage import generate_page
from textnode import TextNode
from copystatic import copy_static


def main():
    source_root = "./static"
    destination_root = "./public"
    print(f"Cleaning project root at {destination_root}...")
    if exists(destination_root):
        rmtree(destination_root)
    print(f"Copying from {source_root} to {destination_root}...")
    copy_static(source_root, destination_root)
    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "./public/index.html"
    generate_page(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()
