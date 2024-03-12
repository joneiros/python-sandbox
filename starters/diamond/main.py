#!/usr/bin/env python3

import diamond as d
import sys



def main():
    argv = sys.argv
    instr = argv[1] if len(argv) > 1 and argv[1].isdecimal() else input("Diamond Raduis?\n")
    innum = int(instr)
    dia = d.Diamond()
    linesToPrint = dia.getDiamond(innum)

    for line in linesToPrint:
        print(line)

main()