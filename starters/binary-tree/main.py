#!/usr/bin/env python3

import NumTree as n

def main():
    instr = instr = input("Give at least 5 numbers separated by spaces: ")
    inarr = instr.split(" ")
    innums = [int(x) for x in inarr if x.isdigit()]
    innums.sort()
    print("Sorted Input: {}".format(innums))

    treeBuilder = n.Tree()
    tree = treeBuilder.buildTree(innums)
    tree.traverse()

    """
    fakeNode10 = n.TreeNode(10)
    fakeNode5 = n.TreeNode(5)
    fakeNode15 = n.TreeNode(15)
    fakeNode4 = n.TreeNode(4)
    fakeNode8 = n.TreeNode(8)

    fakeNode10.addChild(fakeNode5)
    fakeNode10.addChild(fakeNode15)
    fakeNode5.addChild(fakeNode4)
    fakeNode5.addChild(fakeNode8)

    fakeNode10.traverse()
    """


main()
