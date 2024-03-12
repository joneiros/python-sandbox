#!/usr/bin/env python3

def main():
    instr = input("Give me numbers and/or words, separated by spaces!")
    inarr = instr.split(" ")

    words = [x for x in inarr if not x.isdigit()]
    print("Here are the words:")
    for w in words:
        print(w)

    if len(words) < 1:
        print("No Words!")
    else:
        print("And the sorted words:")
        words.sort()
        for w in words:
            print(w)

    nums = [x for x in inarr if x.isdigit()]
    print("Here are the numbers:")
    for n in nums:
        print(str(n))

    if len(nums) < 1:
        print("No Words!")
    else:
        print("And the sorted numbers:")
        nums.sort()
        for n in nums:
            print(str(n))

main()