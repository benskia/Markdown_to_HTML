from os import listdir, mkdir
from os.path import exists, join, isfile
from shutil import copy, rmtree
from textnode import TextNode


def main():
    source_directory = "./static"
    destination_directory = "./public"
    copy_static(source_directory, destination_directory)


def copy_static(old_root, new_root):
    rmtree(new_root)
    mkdir(new_root)
    crawl_directory("", ./static)

def crawl_directory(current_path, target_directory)
    ls = get_ls(join(current_path, target_directory))
    for item in ls:
        pass


def get_ls(filepath):
    try:
        ls = listdir(filepath)
        print(ls)
        return ls
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
