from os import listdir, mkdir
from os.path import exists, join, isfile, isdir
from shutil import copy, rmtree
from textnode import TextNode


def main():
    source_root = "./static"
    destination_root = "./public"
    if exists(destination_root):
        rmtree(destination_root)
    copy_static(source_root, destination_root)


def copy_static(target_path, copy_path):
    print(f"Moving to {target_path} and creating {copy_path}...")
    mkdir(copy_path)
    ls = get_ls(target_path)
    for item in ls:
        target_item_path = join(target_path, item)
        copy_item_path = join(copy_path, item)
        if isdir(target_item_path):
            copy_static(target_item_path, copy_item_path)
        elif isfile(target_item_path):
            print(f"Copying {target_item_path} to {copy_item_path}...")
            copy(target_item_path, copy_item_path)
        else:
            print("Item is neither directory nor file.")


def get_ls(filepath):
    try:
        ls = listdir(filepath)
        return ls
    except Exception as e:
        print(e)
        return []


if __name__ == "__main__":
    main()
