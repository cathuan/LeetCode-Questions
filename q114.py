# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.flatten_with_tail(root)

    def flatten_with_tail(self, root):

        if root is None:
            return None

        left_tail = self.flatten_with_tail(root.left)
        right_tail = self.flatten_with_tail(root.right)

        left_head = root.left
        right_head = root.right
        root.left = None
        root.right = None
        tail = root

        if left_head is None:
            assert left_tail is None
        else:
            tail.right = left_head
            tail = left_tail

        if right_head is None:
            assert right_tail is None
        else:
            tail.right = right_head
            tail = right_tail

        return tail
