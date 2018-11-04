import heapq


class MinHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, v):
        heapq.heappush(self.heap, v)

    def pop(self):
        return heapq.heappop(self.heap)

    def getMin(self):
        if not self.heap:
            return None
        return self.heap[0]

    def getLength(self):
        return len(self.heap)


class MaxHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, v):
        heapq.heappush(self.heap, -v)

    def pop(self):
        return -heapq.heappop(self.heap)

    def getMax(self):
        if not self.heap:
            return None
        return -self.heap[0]

    def getLength(self):
        return len(self.heap)


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """

        self.upperHeap = MinHeap()
        self.lowerHeap = MaxHeap()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """

        if self.upperHeap.getLength() == self.lowerHeap.getLength():
            if num < self.upperHeap.getMin():
                self.lowerHeap.push(num)
                maxValue = self.lowerHeap.pop()
                self.upperHeap.push(maxValue)
            else:
                self.upperHeap.push(num)
        else:
            if num > self.lowerHeap.getMax():
                self.upperHeap.push(num)
                minValue = self.upperHeap.pop()
                self.lowerHeap.push(minValue)
            else:
                self.lowerHeap.push(num)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.upperHeap.getLength() == self.lowerHeap.getLength():
            return (
                self.upperHeap.getMin() + self.lowerHeap.getMax()) * 1.0 / 2
        else:
            return float(self.upperHeap.getMin())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()