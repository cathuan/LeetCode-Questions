# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec(object):

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if root is None:
            return ""

        ret = str(root.val)
        if len(root.children):
            childNodes = []
            for child in root.children:
                childNodes.append(self.serialize(child))
            childStrs = "(" + ",".join(childNodes) + ")"
            ret += childStrs
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        if "(" not in data:
            node = Node(int(data), [])
        else:
            i = 0
            j = 0
            while data[j] != "(":
                j += 1
            token = data[i:j]
            children = self.deserializeChildren(data[j:])
            node = Node(int(token), children)
        return node

    def deserializeChildren(self, data):
        assert data[0] == "("
        assert data[-1] == ")"
        tokens = self.splitToken(data)
        nodes = []
        for token in tokens:
            node = self.deserialize(token)
            nodes.append(node)
        return nodes

    def splitToken(self, data):
        assert data[0] == "("
        assert data[-1] == ")"
        data = data[1:-1]
        bracketCount = 0
        i, j, ret = 0, 0, []
        while j < len(data):
            w = data[j]
            if w == "(":
                bracketCount += 1
            elif w == ")":
                bracketCount -= 1
            elif w == ",":
                if bracketCount == 0:
                    ret.append(data[i:j])
                    i = j + 1
            j += 1
        ret.append(data[i:])
        return ret


if __name__ == "__main__":
    codec = Codec()
    print codec.splitToken("(3(5,6),2,4)")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
