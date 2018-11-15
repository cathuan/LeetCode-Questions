# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return ""

        nodes = [root]
        codes = [str(root.val)]
        while len(nodes) != 0:
            nodes, new_codes = self.expand(nodes)
            codes.extend(new_codes)

        # remove unnecessary None at the end
        node = codes.pop()
        while node == "None":
            node = codes.pop()
        codes.append(node)
        data = "$".join(codes)
        return data

    def expand(self, nodes):

        new_nodes = []
        codes = []
        for node in nodes:
            if node.left is not None:
                new_nodes.append(node.left)
                codes.append(str(node.left.val))
            else:
                codes.append("None")
            if node.right is not None:
                new_nodes.append(node.right)
                codes.append(str(node.right.val))
            else:
                codes.append("None")
        return new_nodes, codes

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == "":
            return None

        codes = data.split("$")
        index = 1
        root = TreeNode(int(codes[0]))
        nodes = [root]

        while index < len(codes):
            nodes, index = self.extend(nodes, index, codes)
        return root

    def extend(self, nodes, index, codes):

        new_nodes = []
        for node in nodes:
            if index < len(codes) and codes[index] != "None":
                node.left = TreeNode(int(codes[index]))
                new_nodes.append(node.left)
            else:
                node.left = None
            index += 1

            if index < len(codes) and codes[index] != "None":
                node.right = TreeNode(int(codes[index]))
                new_nodes.append(node.right)
            else:
                node.right = None
            index += 1
        return new_nodes, index


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
