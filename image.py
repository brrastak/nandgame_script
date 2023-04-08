# get picture description from file specified in command line
# "*" means colored pixel and "-" - transparent one

import sys


def get():
    if len(sys.argv) > 1:
        src_file_name = sys.argv[1]
    else:
        print("""This script produces assembly language code to draw picture for nandgame.com.
You should specify name of file with image description where "*" means colored pixel and "-" - the transparent one.""")
        sys.exit()

    with open(src_file_name, "r") as src_file:
        lines = src_file.readlines()

    lines = ["".join(char for char in line if char in "*-")
             for line in lines if "*" in line or "-" in line]

    return lines