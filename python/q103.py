# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ret = []

        if not root:
            return ret

        # order == True: left to right
        # order == False: right to left
        order = True

        stack = []
        stack.append(root)

        while stack:
            tmpRet = []
            tmpStack = []
            while stack:
                node = stack.pop()
                tmpRet.append(node.val)
                if order:
                    if node.left:
                        tmpStack.append(node.left)
                    if node.right:
                        tmpStack.append(node.right)
                else:
                    if node.right:
                        tmpStack.append(node.right)
                    if node.left:
                        tmpStack.append(node.left)
            stack = tmpStack
            ret.append(tmpRet)
            order = not order

        return ret
