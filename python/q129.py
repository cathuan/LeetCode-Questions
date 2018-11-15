# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        sum, _ = self.sumSubTree(root)
        return sum

    def sumSubTree(self, node):
        if node is None:
            return 0, 0

        sum = 0
        mul = 0

        left_value, left_mul = self.sumSubTree(node.left)
        sum += left_value
        mul += left_mul

        right_value, right_mul = self.sumSubTree(node.right)
        sum += right_value
        mul += right_mul

        if mul == 0:
            assert node.left is None and node.right is None
            assert sum == 0
            mul = 1
        sum += mul * node.val
        return sum, mul * 10
