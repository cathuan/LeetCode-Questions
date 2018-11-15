# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = deque()
        stack.append((root, 1))
        while stack:
            node, lv = stack.popleft()
            if node.left is None and node.right is None:
                return lv

            if node.left is not None:
                stack.append((node.left, lv + 1))
            if node.right is not None:
                stack.append((node.right, lv + 1))
