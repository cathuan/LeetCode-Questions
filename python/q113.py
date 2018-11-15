# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
# 75.37%
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        if root.left is None and root.right is None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []


        left_list = self.pathSum(root.left, sum-root.val)
        right_list = self.pathSum(root.right, sum-root.val)

        result = []
        for subsum in left_list:
            result.append([root.val] + subsum)

        for subsum in right_list:
            result.append([root.val] + subsum)

        return result
