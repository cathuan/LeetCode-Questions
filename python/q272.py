# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __init__(self):
        self.preStack = []
        self.sucStack = []

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """

        self.initPreStack(root, target)
        self.initSucStack(root, target)
        if self.preStack and self.sucStack and self.preStack[-1].val == self.sucStack[-1].val == target:
            self.getSuccessor()

        prevValue = self.preStack[-1].val if self.preStack else float("-inf")
        nextValue = self.sucStack[-1].val if self.sucStack else float("inf")
        ret = []
        #print prevValue, nextValue
        #print "* prev", [node.val for node in self.preStack]
        #print "* succ", [node.val for node in self.sucStack]
        while len(ret) < k:
            prevDif = target - prevValue
            nextDif = nextValue - target
            if prevDif <= nextDif:
                ret.append(prevValue)
                self.getPredecessor()
                prevValue = self.preStack[-1].val if self.preStack else float("-inf")
            else:
                ret.append(nextValue)
                self.getSuccessor()
                nextValue = self.sucStack[-1].val if self.sucStack else float("inf")
            #print prevValue, nextValue
            #print "* prev", [node.val for node in self.preStack]
            #print "* succ", [node.val for node in self.sucStack]
        return ret

    def initPreStack(self, root, target):
        node = root
        while node:
            if node.val == target:
                self.preStack.append(node)
                break
            elif node.val > target:
                node = node.left
            else:
                self.preStack.append(node)
                node = node.right
        #print "prevStack", [node.val for node in self.preStack]

    def initSucStack(self, root, target):
        node = root
        while node:
            if node.val == target:
                self.sucStack.append(node)
                break
            elif node.val > target:
                self.sucStack.append(node)
                node = node.left
            else:
                node = node.right

    # Find the previous corresponding node based on the stack.
    def getPredecessor(self):
        node = self.preStack.pop()
        value = node.val
        node = node.left
        while node:
            self.preStack.append(node)
            node = node.right
        return value

    # Find the next corresponding node based on the stack.
    def getSuccessor(self):
        node = self.sucStack.pop()
        value = node.val
        node = node.right
        while node:
            self.sucStack.append(node)
            node = node.left
        return value
