#!/usr/bin/env python3

import sys

def main():
    argv = sys.argv
    print("First index of x in y")
    toFind = argv[1] if len(argv) > 1 else input("What "
         + "are you searching for?\n")
    searchSpace = argv[2] if len(argv) > 2 else input("What "
         + "are you searching in?\n")

    found = searchSpace.find(toFind)
    if found < 0:
        print("Not Found!")
    else:
        print("Found at index: " + str(found))

main()