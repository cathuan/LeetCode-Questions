# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        _, max_path = self.maxPathToRoot(root)
        return max_path

    def maxPathToRoot(self, root):

        if root is None:
            return 0, float("-inf")

        l, max_path_l = self.maxPathToRoot(root.left)
        r, max_path_r = self.maxPathToRoot(root.right)
        if l < 0:
            l = 0
        if r < 0:
            r = 0
        max_path = max(max_path_l, max_path_r, l+r+root.val)
        return max(l+root.val, r+root.val), max_path