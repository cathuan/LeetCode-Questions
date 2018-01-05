# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        nodes = [root]
        new_nodes = self.expand(nodes)
        while len(new_nodes) != 0:
            nodes = new_nodes
            new_nodes = self.expand(nodes)
        return nodes[0].val

    def expand(self, nodes):

        new_nodes = []
        for node in nodes:
            if node.left is not None:
                new_nodes.append(node.left)
            if node.right is not None:
                new_nodes.append(node.right)
        return new_nodes
