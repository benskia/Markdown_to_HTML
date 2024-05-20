from os import path, listdir, mkdir
from shutil import copy, rmtree
from textnode import TextNode


def main():
    source_directory = "./static"
    desination_directory = "./public"
    build_static_site_project(source_directory, desination_directory)


def build_static_site_project(source, destination):
    rmtree(destination)
    mkdir(destination)
    ls = get_ls(source)
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
