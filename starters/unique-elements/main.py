#!/usr/bin/env python3

def main():
    elements = [1, 3, 3, 4, 1, 2]
    repeatedElements = []

    for element in elements:
        #temporarily remove one instance of element
        elements.remove(element)

        #check if element still exists after being removed once
        if element in elements:
            repeatedElements.append(element)
            #re-add element to avoid false positives in other places in the loop
            elements.append(element)
            continue

    nonRepeatedElements = [ x for x in elements if x not in repeatedElements ]

    print(nonRepeatedElements)

main()