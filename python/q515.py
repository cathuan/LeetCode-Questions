# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = []
        stack.append(root)
        ret = []
        while stack:
            nextStack = []
            maxValue = float("-inf")
            while stack:
                node = stack.pop()
                maxValue = max(maxValue, node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            stack = nextStack
            ret.append(maxValue)
        
        return ret