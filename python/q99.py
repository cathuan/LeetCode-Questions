# Answer: https://leetcode.com/problems/recover-binary-search-tree/discuss/187407/Python-short-and-slick-solution-(108ms-beats-100)-both-stack-and-Morris-versions
# Need to follow the answer again.

# Morris Inorder Traversal to keep O(1)
# Traverse the binary sort tree in order


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        cur = root
        prev = TreeNode(float('-inf'))
        drops = []

        while cur:
            if cur.left:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                    continue
                tmp.right = None
            if cur.val < prev.val:
                drops.append((prev, cur))
            prev, cur = cur, cur.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val
