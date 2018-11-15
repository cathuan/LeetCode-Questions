#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import numpy as np


# 0.15%
class Solution2(object):

    @profile
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return -1

        if root.left is None:
            # sanity check
            # assert root.right is None
            return -1

        stack = [root]
        root_value = root.val
        min_value = np.inf

        while len(stack) > 0:
            node = stack.pop()

            if node.left is None:
                # sanity check
                # assert node.right is None
                continue
            else:
                if node.left.val > root_value:
                    min_value = min(node.left.val, min_value)
                else:
                    stack.append(node.left)

                if node.right.val > root_value:
                    min_value = min(node.right.val, min_value)
                else:
                    stack.append(node.right)

        result = -1 if min_value == np.inf else min_value
        return result


# even worse speed. Maybe 0%
# and there is a maximum recursive depth.. So if the tree is too big, we can't use this method.
class Solution(object):

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.res = np.inf
        self.traverse(root, root.val)

        result = -1 if self.res == np.inf else self.res
        return result

    def traverse(self, node, root_value):

        if node is None:
            return

        if root_value < node.val < self.res:  # implicitly, root_value < node.val < self.res
            self.res = node.val
            return
        elif root_value == node.val:
            self.traverse(node.left, root_value)
            self.traverse(node.right, root_value)
            return
        else:
            return



if __name__ == "__main__":

    root = TreeNode(2)
    stack = [root]
    for _ in range(100):
        node = stack.pop()
        node.left = TreeNode(2)
        node.right = TreeNode(2)
        stack.append(node.left)
        stack.append(node.right)

    for _ in range(len(stack)):
        node = stack.pop()
        node.left = TreeNode(3)
        node.right = TreeNode(4)

    print Solution().findSecondMinimumValue(root)
    print Solution2().findSecondMinimumValue(root)
