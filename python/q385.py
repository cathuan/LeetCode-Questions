# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        stack = []
        cur = ""
        for w in s:
            if w == "[":
                assert not cur
                stack.append(w)
            elif w == "]":
                if cur:
                    stack.append(NestedInteger(int(cur)))
                    cur = ""

                value = stack.pop()
                nums = []
                while value != "[":
                    nums.append(value)
                    value = stack.pop()

                nums = nums[::-1]
                nestedList = NestedInteger(nums)
                stack.append(nestedList)
            elif w == ",":
                if cur:
                    stack.append(NestedInteger(int(cur)))
                    cur = ""
            else:
                cur += w
        if cur:
            stack.append(NestedInteger(int(cur)))
        return stack[0]


if __name__ == "__main__":

    print Solution().tokenize("[123,[456,[789,736,452,[555,666]]]]")
