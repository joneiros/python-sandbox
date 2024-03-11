#!/usr/bin/env python3

import sys

def main():
    argv = sys.argv
    stdin_var = sys.stdin
    out_var = sys.stdout

    out_var.write("Python command line args: \n")

    #this is the filename command, with filename as it was typed (including "./")
    # if running as an executable from the same directory, or more if running it
    # from elsewhere, and bare if running using the shell command
    # (`python3 fizzbuzz.py`) rather than direct execution strategy
    out_var.write(argv[0] + "\n")

    # out_var.write(argv[1] + "\n") #this is where the optional args start.

    instr = argv[1] if len(argv) > 1 and argv[1].isdecimal() else input("How much to FizzBuzz?\n")
    innum = int(instr)

    #equivalent to print() for the purposes of shell scripts
    out_var.write("You wanna fizzbuzz " + instr + " much!\n")

    for x in range(innum + 1):
        out_var.write(getToPrint(x) + "\n")

def tryGetFizz(fizznum):
    if fizznum % 3 == 0:
        return "Fizz"

    return ""

def tryGetBuzz(buzznum):
    if buzznum % 5 == 0:
        return "Buzz"

    return ""

def getToPrint(tryNum):
    fizzbuzz = tryGetFizz(tryNum) + tryGetBuzz(tryNum)

    return fizzbuzz if fizzbuzz != "" else str(tryNum)

main()