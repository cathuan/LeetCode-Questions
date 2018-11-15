# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest
frequently? How would you optimize the kthSmallest routine?

Idea: Currently, the solution has O(n) complexity, where n = size of the tree. Think about the the
tree [100,99,null,98,null,97,null,...,1,null]. Even k = 1, we need to go down the tree, which
involes c*n operations.

I think the better idea is to maintain a stack S with all the "left nodes" since root, i.e.
S = Stack()
node = root
while node is not None:
    S.push(node)
    node = node.left

and while doing inserting/deleting, we modify the stack accordingly. Note that we only need to push
the Stack if we add a smallest value, or we pop (and maybe push a new node) the stack if we do
deletion. Insertion and deletion will be slower by a constant time.

Then, using the following solution, the process is O(k). We always start from the smallest element.
"""
# TODO: any better idea?

# 79.77%
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
