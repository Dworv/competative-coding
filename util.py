#!/usr/bin/python3

from sys import argv
import os
import time

doc = """
This utility generates new problem folders quickly. New features may be added, 
but for now it only supports the `new` command. 

`new` <path: example/problem_name> <extension: py | cpp> 
This command makes a new directory for a problem, and fails if it already exists.
""".strip()

def subcommand_new(path, extension):
    if os.getcwd().split("/")[-1] != "competative-coding":
        print("This command should only be called from the project root.")
        exit(1)
    path_list = path.split("/")
    for i in range(len(path_list) - 1):
        try:
            os.mkdir(path_list[i])
        except FileExistsError:
            pass
        os.chdir(path_list[i])
    
    try:
        os.mkdir(path_list[-1])
    except FileExistsError:
        print("Problem directory already exists, stopping.")
        exit(1)
    
    os.chdir(path_list[-1])
    open("".join(path_list) + "." + extension, "x")
    open("input.txt", "x")

if __name__ == "__main__":
    if len(argv) == 1 or argv[1] in ["-h", "--help"]:
        print(doc)

    if argv[1] == "new":
        subcommand_new(argv[2], argv[3])
    else:
        print(doc)