"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0

        stack = []
        stack.append(root)
        level = 1
        while True:
            nextStack = []
            while stack:
                node = stack.pop()
                for child in node.children:
                    nextStack.append(child)
            stack = nextStack
            if not stack:
                break
            level += 1
        
        return level