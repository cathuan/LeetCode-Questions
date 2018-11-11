import heapq
from collections import defaultdict, deque


class Heap(object):

    def __init__(self):
        self.heap = []
        self.deactivated = defaultdict(int)
        self.deactivatedCounts = 0

    def push(self, v):
        assert False

    def pop(self):
        assert False

    def getLength(self):
        return len(self.heap)

    def getActiveLength(self):
        return len(self.heap) - self.deactivatedCounts

    def clean(self):
        #print "Before Clean", self.deactivated
        while len(self.heap) > 0 and self.deactivated[self.heap[0]] > 0:
            #print "Cleaning", self.heap[0], self.deactivated[self.heap[0]]
            self.deactivated[self.heap[0]] -= 1
            self.pop()
            self.deactivatedCounts -= 1


class MinHeap(Heap):

    def push(self, v):
        heapq.heappush(self.heap, v)

    def pop(self):
        return heapq.heappop(self.heap)

    def getMin(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def deactive(self, v):
        self.deactivated[v] += 1
        self.deactivatedCounts += 1


class MaxHeap(Heap):

    def push(self, v):
        heapq.heappush(self.heap, -v)

    def pop(self):
        return -heapq.heappop(self.heap)

    def getMax(self):
        if len(self.heap) == 0:
            return None
        return -self.heap[0]

    def deactive(self, v):
        self.deactivated[-v] += 1
        self.deactivatedCounts += 1


class MedianSlidingWindow(object):

    def __init__(self, length):

        self.data = deque()
        self.length = length
        self.lowerHeap = MaxHeap()
        self.upperHeap = MinHeap()

    def push(self, v):

        self.data.append(v)
        lo = self.lowerHeap.getMax()
        if v > lo:
            self.upperHeap.push(v)
        else:
            self.lowerHeap.push(v)
        self.pop()
        assert 0 <= self.upperHeap.getActiveLength() - self.lowerHeap.getActiveLength() <= 1

    def balance(self):
        while self.upperHeap.getActiveLength() < self.lowerHeap.getActiveLength():
            newValue = self.lowerHeap.pop()
            self.upperHeap.push(newValue)

        while self.upperHeap.getActiveLength() > self.lowerHeap.getActiveLength() + 1:
            newValue = self.upperHeap.pop()
            self.lowerHeap.push(newValue)

        self.upperHeap.clean()
        self.lowerHeap.clean()
        assert 0 <= self.upperHeap.getActiveLength() - self.lowerHeap.getActiveLength() <= 1

    def pop(self):
        while len(self.data) > self.length:
            v = self.data.popleft()
            #print "POP", v
            lo = self.lowerHeap.getMax()
            if v <= lo:
                self.lowerHeap.deactive(v)
            else:
                self.upperHeap.deactive(v)
        self.balance()
        assert 0 <= self.upperHeap.getActiveLength() - self.lowerHeap.getActiveLength() <= 1

    def getMedian(self):
        assert 0 <= self.upperHeap.getActiveLength() - self.lowerHeap.getActiveLength() <= 1
        if self.lowerHeap.getActiveLength() == self.upperHeap.getActiveLength():
            lo = self.lowerHeap.getMax()
            hi = self.upperHeap.getMin()
            #print "median balanced", lo, hi, (lo+hi)*1.0/2
            #print self.upperHeap.heap
            #print self.lowerHeap.heap
            return (lo+hi)*1.0/2
        else:
            assert self.lowerHeap.getActiveLength() == self.upperHeap.getActiveLength()-1
            #print "median inbalanced", self.upperHeap.getMin(), self.lowerHeap.getActiveLength(), self.upperHeap.getActiveLength()
            #print self.upperHeap.heap
            #print self.lowerHeap.heap
            return self.upperHeap.getMin()*1.0


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """

        window = MedianSlidingWindow(k)
        for i in range(k-1):
            window.push(nums[i])

        medians = []
        for i in range(k-1, len(nums)):
            window.push(nums[i])
            median = window.getMedian()
            medians.append(median)

        return medians


if __name__ == "__main__":
    print Solution().medianSlidingWindow([7, 0, 3, 9, 9, 9, 1, 7, 2, 3], 6)
