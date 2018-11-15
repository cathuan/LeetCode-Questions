class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.data = []
        self.min_values = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        if len(self.min_values) == 0:
            self.min_values.append(x)
        else:
            self.min_values.append(min(self.min_values[-1], x))
        self.data.append(x)


    def pop(self):
        """
        :rtype: void
        """

        self.data.pop()
        self.min_values.pop()

    def top(self):
        """
        :rtype: int
        """

        return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """

        return self.min_values[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
