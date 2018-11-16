class FreqStack(object):

    def __init__(self):
        self.stacks = {}
        self.freqs = {}
        self.maxFreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        if x not in self.freqs:
            self.freqs[x] = []
        freq = len(self.freqs[x])+1
        self.freqs[x].append(freq)
        self.maxFreq = max(self.maxFreq, freq)

        if freq not in self.stacks:
            self.stacks[freq] = []
        self.stacks[freq].append(x)

    def pop(self):
        """
        :rtype: int
        """

        x = self.stacks[self.maxFreq].pop()
        self.freqs[x].pop()
        if len(self.stacks[self.maxFreq]) == 0:
            del self.stacks[self.maxFreq]
            self.maxFreq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
