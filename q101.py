# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        return self.compare(root.left, root.right)

    def compare(self, root1, root2):

        if root1 is None:
            return root1 == root2

        if root2 is None:
            return root1 == root2

        if root1.val != root2.val:
            return False

        if not self.compare(root1.left, root2.right):
            return False
        else:
            return self.compare(root1.right, root2.left)
