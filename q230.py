# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 79.77%
# TODO: but if the BST is inserting/deleting often, how can we get this quickly? This is O(n)..
class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        assigned_nodes = {}
        node_count = 0
        stack = [root]

        while len(stack) > 0:
            node = stack[-1]

            # sanity check
            #assert node not in assigned_nodes
            #assert node is not None

            if node.left is None or node.left in assigned_nodes:
                node_count += 1
                assigned_nodes[node] = node_count
                if node_count == k:
                    return node.val
                stack.pop()
                if node.right is not None:
                    stack.append(node.right)
                continue
            elif node.left not in assigned_nodes:
                stack.append(node.left)
                continue
            else:
                assert False

        assert False, "We have run over all the nodes. Seems the number of nodes < k."
