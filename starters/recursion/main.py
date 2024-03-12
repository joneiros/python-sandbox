#!/usr/bin/env python3

import sys

def main():
    argv= sys.argv

    instr = argv[1] if len(argv) >= 2 and argv[1].isdigit() else input("Count down from...? ")
    down = int(instr)
    print("Regular Countdown")
    countdown(down)

    print("Recursive Countdown")
    recursiveCountdown(down)

def countdown(down):
    for x in range(down, -1, -1):
        print(x)

def recursiveCountdown(down):
    if down < 0:
        print("Below 0!")
    elif down == 0:
        print(0)
    else:
        print(down)
        recursiveCountdown(down - 1)


main()