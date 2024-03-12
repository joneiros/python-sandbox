
class Tree:
    def __init__(self):
        self.treeNodes = []

    def buildTree(self, items):
        if len(items) == 0:
            return "No Child"

        midIndex = len(items) // 2 # / divides and gives float, // floors, giving int
        midVal = items[midIndex]
        print("Middle index: {0}".format(midIndex))
        print("Middle value: {0}".format(midVal))

        node = TreeNode(midVal)
        node.addChild(self.buildTree(items[ : midIndex]))
        node.addChild(self.buildTree(items[midIndex + 1 :]))

        return node


class TreeNode:
    nodes = None

    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, childNode):
        if childNode == "No Child":
            print(childNode)
            return

        print("Adding child: " + str(childNode.value))
        self.children.append(childNode)

    def removeChild(self, childNode):
        print("Removing child node " +str(childNode.value) + " from " + str(self.value))
        self.children = [child for child in self.children if child is not childNode]

    def traverse(self):
        nodesToVisit = [self]
        while len(nodesToVisit) > 0:
            currentNode = nodesToVisit.pop()
            child1 = currentNode.children[0].value if len(currentNode.children) > 0 else "No Child"
            child2 = currentNode.children[1].value if len(currentNode.children) > 1 else "No Child"
            print( "Visiting " + str(currentNode.value) + " with children " + str(child1) + " and "  + str(child2) )

            nodesToVisit += currentNode.children




