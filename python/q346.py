class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        
        self.size = size
        self.buffer = []
        self.current_sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        self.buffer.append(val)
        self.current_sum += val
        if len(self.buffer) > self.size:
            popedValue = self.buffer.pop(0)
            self.current_sum -= popedValue

        return self.current_sum * 1.0 / len(self.buffer)
        
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)